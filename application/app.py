
from flask import Flask, render_template, request, redirect, url_for, flash,session, g
import logging
from logging import Formatter, FileHandler
from forms import *
import pymongo
from forms import LoginForm
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from src.database import user_model
from flask.ext.login import LoginManager
from user import User
from src.kube_api import manage_app, namespace, default_config, default_limits, quotas, kube_svc, helm_proxy
import requests
import flask_admin as admin
from flask_admin.contrib.pymongo import ModelView, filters
from wtforms import form, fields
from bson.objectid import ObjectId
from werkzeug.local import LocalProxy
from pymongo import MongoClient
app = Flask(__name__)
# app.config['MONGO_HOST']='127.0.0.1'
# app.config['MONGO_PORT']='27017'
# app.config['MONGO_DBNAME']='app_db'

app.config.from_object('config.BaseConfig')
conn = pymongo.Connection()
db=conn.app_db
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/catalog')
def catalog():
    application_catalog = db.catalog.find()
    return render_template('pages/catalog.html',application_catalog=application_catalog)

@app.route('/profile')
@login_required
def profile():
    endpoints=[]
    applications=[]
    # try:
    #
    #
    #
    # except:
    #     flash("Unable to connect to API server")
    # #applications=db.catalog.find()
    user_services = kube_svc.list_namespaced_services(current_user.username)
    nodes = kube_svc.get_nodes()
    for service in user_services:
        # flash("key: {key} value: {value}".format(key=service['name'], value=service['port']))
        url = None
        if service['type'] == 'NodePort':
            url = 'http://{ip}:{port}'.format(ip=nodes[0]['ip'], port=service['port'])
        endpoints.append({
            'name': service['name'],
            'type': service['type'],
            'age': '1day',
            'url': url
        })
        app_db = service['name'].split('-')[1]
        app = db.catalog.find_one({'name': app_db})
        if app is not None:
            applications.append({
                'title': app['title'],
                'subtitle': app['subtitle'],
                'icon': app['icon'],
                'name': app['name']
            })
    resources=[{'name':'CPU','type':'hardware','request':'1','limit':'2'},
    {'name':'CPU','type':'hardware','request':'1','limit':'2'},
    {'name':'CPU','type':'hardware','request':'1','limit':'2'}]
    # endpoints=[{'name':'CPU','type':'hardware','age':'1','url':'http://apps.namal.edu.pk/username/userapp'},
    # {'name':'CPU','type':'hardware','age':'1','url':'http://apps.namal.edu.pk/username/userapp'},
    # {'name':'CPU','type':'hardware','age':'1','url':'http://apps.namal.edu.pk/username/userapp'}]
    return render_template('pages/profile.html',applications=applications,resources=resources,endpoints=endpoints)

@app.route('/catalog/<name>/details')
def details(name):
    app_detail=db.catalog.find_one({'name':name})
    app_detail={'title':app_detail['title'],
                'subtitle':app_detail['subtitle'],
                'icon': "/"+app_detail['icon'],
                'details':app_detail['details'],
                'url':app_detail['docker_compose'],
                'name': app_detail['name'],
                'label': app_detail['label']}
    return  render_template('pages/detail.html',app=app_detail)


@app.route('/catalog/<name>/launch')
@login_required
def launch_kubeapp(name):
    username=current_user.username
    application =db.catalog.find_one({'name':name})
    if application is not None:
        chart = application['chart']
        app_name=username+"-"+application['name']
        app_namespace=username
        app_type="NodePort"
        if helm_proxy.exist(app_namespace,app_name):
            flash("Application Already Installed")
        elif chart is not None:
            response=helm_proxy.install(chart,app_namespace,app_name,app_type)
            flash(response)
    #manage_app.install_app('jupyterhub','https://jupyterhub.github.io/helm-chart/jupyterhub-v0.6.tgz','user-321','type: NodePort')
    return redirect(url_for("profile"))

@app.route('/catalog/<name>/remove')
@login_required
def remove_kubeapp(name):
    app_name=current_user.username+"-"+name
    response=helm_proxy.uninstall(app_name)
    if response==200:
        flash("%s uninsatlled"%app_name)
    else:
        flash("unable to remove %s"%app_name)
    return redirect(url_for("profile"))
@app.route('/catalog/add_app', methods=['GET','POST'])
def add_app():
    # form = form = RegisterForm(request.form)
    return render_template('forms/add.html')

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


@app.route('/register', methods=['POST', 'GET'])
def register():
    users = db.users
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            password = request.form['password']
            password=generate_password_hash(password, method='pbkdf2:sha256')
            users.insert({'name': request.form['username'], 'password': password})
            session['username']=request.form['username']
            user_namespace=namespace.create_namespace(session['username'])
            if user_namespace==201:
                flash("Namespace created successfully")
            return redirect(url_for('profile'))
        flash ('User already exist head towards login')
            # return 'That username already exists!'
    return render_template('forms/register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = db.users.find_one({"name": request.form['username']})
        if user and User.validate_login(user['password'], request.form['password']):
            user_obj = User(user['name'])
            login_user(user_obj)
            user_workspace=(user['name'])
            try:
                if not namespace.is_namespace_exist(user_workspace):
                    if namespace.create_namespace(user_workspace) == 201:
                        flash("workspace created successfully")
            except requests.exceptions.RequestException:
                flash("Unable to connect to API server")
            return redirect(request.args.get("next") or url_for("profile"))
        flash("Wrong username or password!", category='error')
    return render_template('forms/login.html', title='login')

@lm.user_loader
def load_user(username):
    u = db.users.find_one({"name": username})
    if not u:
        return None
    return User(u['name'])

@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return 'we are prtecting you'





# User admin
class UserForm(form.Form):
    name = fields.StringField('Name')
    title = fields.StringField('Title')
    subtitle = fields.StringField('Subtitle')
    details = fields.StringField('Details')
    label = fields.TextField('Label')
    chart = fields.StringField('Chart URL')
    icon = fields.StringField('Icon URL')
    docker_compose = fields.StringField('docker-compose file URL')

class AdminView(ModelView):
    column_list = ('name', 'title', 'subtitle','details','label','chart','docker_compose','icon')
    column_sortable_list = ('name', 'title', 'subtitle')

    form = UserForm

    def on_model_change(self, form, model):
        user_id = model.get('user_id')
        model['user_id'] = ObjectId(user_id)
        return model
    # def is_accessible(self):
    #     current_user.has_role('admin')


if __name__ == '__main__':
    admin = admin.Admin(app, name='Admin')
    admin.add_view(AdminView(db.catalog, 'Manage'))
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''