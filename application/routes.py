from application import app
import sqlite3
from flask import Flask, render_template, g, request, redirect, flash, session
import json
import sqlite3
import os
import re


DATABASE = 'levels.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def datastuff():
    return render_template("editor.html")


@app.route('/upload',methods=['GET', 'POST'])
def uploadlvl():
    if request.method == 'POST':
        file = request.files['file']
        get_db()
        cursor = get_db().cursor()
        cursor.execute(file)
        get_db().commit()
        

        return f'Uploaded: {file.filename}'
    return render_template('editor.html')


@app.route('/data')
def getLevels():
    #stats display for one user
    cursor = get_db().cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("levels.html", results=results)


@app.route('/download')
def downloadOnline():
    id = request.form.get("levelname")
    cursor = get_db().cursor()
    sql = "SELECT level FROM user WHERE id="

        