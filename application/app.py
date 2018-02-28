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
    return "<h1>User inserted</h1>"
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
        'sub_title':'Java IDE',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'LibreOffice Writer',
        'sub_title':'Document Editors',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'LibreOffice Calculator',
        'sub_title':'Office Suite',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'LibreOffice Draw',
        'sub_title':'Drawing Tool',
        'url':'#', 
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'LibreOffice Impress',
        'sub_title':'Presentation Editors/Maker',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'Pycharm Community Edition',
        'sub_title':'IDE for Python',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'Intellij Idea Community Edition',
        'sub_title':'IDE for java',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'Scratch',
        'sub_title':'Programming for Kids',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'VLC videolan Media Player',
        'sub_title':'Media Player',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'wireshark',
        'sub_title':'Network Debugging Tool',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    },
    {
        'title': 'Inkspace',
        'sub_title':'Image Editor',
        'url':'#',
        'icon':'static/ico/apple-touch-icon-114-precomposed.png'
    }]
    '''
    payload=[{
        'title': 'Eclipse',
        'sub_title':'Java IDE',
        'url':'#',
        'icon':'static/ico/app-icons/arduino-icon.png'
    },
    {
        'title': 'LibreOffice Writer',
        'sub_title':'Document Editors',
        'url':'#',
        'icon':'static/ico/app-icons/blender-icon.png'
    },
    {
        'title': 'LibreOffice Calculator',
        'sub_title':'Office Suite',
        'url':'#',
        'icon':'static/ico/app-icons/eclipse-icon.png'
    },
    {
        'title': 'LibreOffice Draw',
        'sub_title':'Drawing Tool',
        'url':'#', 
        'icon':'static/ico/app-icons/firefox-logo.png'
    },
    {
        'title': 'LibreOffice Impress',
        'sub_title':'Presentation Editors/Maker',
        'url':'#',
        'icon':'static/ico/app-icons/gimp.png'
    },
    {
        'title': 'Pycharm Community Edition',
        'sub_title':'IDE for Python',
        'url':'#',
        'icon':'static/ico/app-icons/inkscape.png'
    },
    {
        'title': 'Intellij Idea Community Edition',
        'sub_title':'IDE for java',
        'url':'#',
        'icon':'static/ico/app-icons/intellij-icon.png'
    },
    {
        'title': 'Scratch',
        'sub_title':'Programming for Kids',
        'url':'#',
        'icon':'static/ico/app-icons/libreoffice_calc.png'
    },
    {
        'title': 'VLC videolan Media Player',
        'sub_title':'Media Player',
        'url':'#',
        'icon':'static/ico/app-icons/vlc.png'
    },
    {
        'title': 'wireshark',
        'sub_title':'Network Debugging Tool',
        'url':'#',
        'icon':'static/ico/app-icons/wireshark.png'
    },
    {
        'title': 'Inkspace',
        'sub_title':'Image Editor',
        'url':'#',
        'icon':'static/ico/app-icons/libreoffice_draw.png'
    },
    {
        'title': 'Gimp',
        'sub_title':'Image Editor',
        'url':'#',
        'icon':'static/ico/app-icons/libreofficewirter.png'
    },
    {
        'title': 'Firefox',
        'sub_title':'Browser',
        'url':'#',
        'icon':'static/ico/app-icons/pycharm-icon.png'
    },
    {
        'title': 'Arduino',
        'sub_title':'Electrical Stuff',
        'url':'#',
        'icon':'static/ico/app-icons/libreoffice_present.png'
    },
    {
        'title': 'Blender',
        'sub_title':'Graphic and 3D',
        'url':'#',
        'icon':'static/ico/app-icons/scratch.png'
    }
    ]
    '''
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