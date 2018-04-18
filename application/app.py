
from flask import Flask, render_template, request, redirect, url_for, flash,session, g
import logging
from logging import Formatter, FileHandler
from forms import *
from flask_pymongo import PyMongo
from forms import LoginForm
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from src.database import user_model
from flask.ext.login import LoginManager
from user import User
from src.kube_api import manage_app, namespace, default_config, default_limits, quotas
app = Flask(__name__)
# app.config['MONGO_HOST']='127.0.0.1'
# app.config['MONGO_PORT']='27017'
# app.config['MONGO_DBNAME']='app_db'
app.config.from_object('config')
mongo = PyMongo(app,config_prefix='MONGO')
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
    application_catalog = mongo.db.catalog.find()
    return render_template('pages/catalog.html',application_catalog=application_catalog)

@app.route('/profile')
def profile():
    applications = mongo.db.catalog.find()
    # send resources adn endpoints
    resources=[{'name':'CPU','type':'hardware','request':'1','limit':'2'},
    {'name':'CPU','type':'hardware','request':'1','limit':'2'},
    {'name':'CPU','type':'hardware','request':'1','limit':'2'}]
    endpoints=[{'name':'CPU','type':'hardware','age':'1','url':'http://apps.namal.edu.pk/username/userapp'},
    {'name':'CPU','type':'hardware','age':'1','url':'http://apps.namal.edu.pk/username/userapp'},
    {'name':'CPU','type':'hardware','age':'1','url':'http://apps.namal.edu.pk/username/userapp'}]
    return render_template('pages/profile.html',applications=applications,resources=resources,endpoints=endpoints)

@app.route('/catalog/<name>/details')
def details(name):
    app_detail=mongo.db.catalog.find_one({'name':name})
    app_detail={'title':app_detail['title'],
                'subtitle':app_detail['subtitle'],
                'icon': "/"+app_detail['icon'],
                'details':app_detail['details']}
    return  render_template('pages/detail.html',app=app_detail)


@app.route('/catalog/<name>/launch')
@login_required
def launch_kubeapp(name):
    username=current_user.username
    manage_app.install_app('jupyterhub','https://jupyterhub.github.io/helm-chart/jupyterhub-v0.6.tgz','user-321','type: NodePort')
    return render_template('pages/home.html')

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
    users = mongo.db.users
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            password = request.form['password']
            password=generate_password_hash(password, method='pbkdf2:sha256')
            users.insert_one({'name': request.form['username'], 'password': password})
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        flash ('User already exist head towards login')
            # return 'That username already exists!'
    return render_template('forms/register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = mongo.db.users.find_one({"name": request.form['username']})
        if user and User.validate_login(user['password'], request.form['password']):
            user_obj = User(user['name'])
            login_user(user_obj)
            return redirect(request.args.get("next") or url_for("home"))
        flash("Wrong username or password!", category='error')
    return render_template('forms/login.html', title='login')

@lm.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"name": username})
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

if __name__ == '__main__':
    app.run(debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''