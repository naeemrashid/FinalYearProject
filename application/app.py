#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, redirect, url_for
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from flask_pymongo import PyMongo


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
mongo = PyMongo(app)
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')
@app.route('/catalog')
def catalog():
    application_catalog = mongo.db.catalog.find()
    return render_template('pages/catalog.html',application_catalog=application_catalog)

@app.route('/add')
def add():
    # payload={
    #     'title': 'eclipse',
    #     'sub_title':'Java IDE by eclipse platform',
    #     'url':'https://www.eclipse.com',
    #     'icon':'static/ico/libreoffice_writer_128.jpg'
    # }
    payload=generate_payload()
    mongo.db.catalog.insert_many(payload)
    return "User inserted"
@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)
@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


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
#----------------------------------------------------------------------------#
# Generate Some Payload
#----------------------------------------------------------------------------#

def generate_payload():
    payload=[{
        'title': 'Eclipse',
        'sub_title':'Java IDE by eclipse platform',
        'url':'#',
        'icon':'static/ico/eclipse_128.png'
    },
    {
        'title': 'LibreOffice Writer',
        'sub_title':'Open Source Document Editors',
        'url':'#',
        'icon':'static/ico/libreoffice_writer_128.jpg'
    },
    {
        'title': 'LibreOffice Calculator',
        'sub_title':'Open Source Office Suite for .csv files',
        'url':'#',
        'icon':'static/ico/libreoffice_calc_128.jpg'
    },
    {
        'title': 'LibreOffice Draw',
        'sub_title':'Open Source Drawing Tool',
        'url':'#',
        'icon':'static/ico/libreoffice_draw_128.png'
    },
    {
        'title': 'LibreOffice Impress',
        'sub_title':'Open Source Document Presentation Editors/Maker',
        'url':'#',
        'icon':'static/ico/libreoffice_present_128.png'
    },
    {
        'title': 'Pycharm Community Edition',
        'sub_title':'Open Source IDE for Python Development',
        'url':'#',
        'icon':'static/ico/pycharm_128.png'
    },
    {
        'title': 'Intellij Idea Community Edition',
        'sub_title':'Open Source IDE for java Development',
        'url':'#',
        'icon':'static/ico/idea_128.png'
    },
    {
        'title': 'Scratch',
        'sub_title':'Open Source Code Block Editor for Kids',
        'url':'#',
        'icon':'static/ico/scratch_128.jpg'
    },
    {
        'title': 'VLC videolan Media Player',
        'sub_title':'Open Source Media Player by videolan',
        'url':'#',
        'icon':'static/ico/vlc_128.jpg'
    },
    {
        'title': 'wireshark',
        'sub_title':'Open Source Network Debugging Tool',
        'url':'#',
        'icon':'static/ico/wireshark_128.png'
    },
    {
        'title': 'Inkspace',
        'sub_title':'Open Source Image Editor',
        'url':'#',
        'icon':'static/ico/inkspace_128.png'
    },
    {
        'title': 'Gimp',
        'sub_title':'Open Source Image Editor',
        'url':'#',
        'icon':'static/ico/gimp_128.jpg'
    },
    {
        'title': 'Firefox',
        'sub_title':'Open Source Browser',
        'url':'#',
        'icon':'static/ico/firefox_128.jpg'
    },
    {
        'title': 'Arduino',
        'sub_title':'Electrical Stuff',
        'url':'#',
        'icon':'static/ico/arduino_128.png'
    },
    {
        'title': 'blender',
        'sub_title':'Open Source Graphic and 3D printing tool',
        'url':'#',
        'icon':'static/ico/blender_128.jpg'
    }
    ]
    return payload

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
