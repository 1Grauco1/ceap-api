from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db= SQLAlchemy()

def init_db(app:Flask):
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///ceap.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
    db.init_app(app)

