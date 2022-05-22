from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'withershieldwhen?'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///levels.db'

db = SQLAlchemy(app)

from application import models
from application import routes
