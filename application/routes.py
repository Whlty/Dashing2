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

# upload level button
@app.route('/upload',methods=['GET', 'POST'])
def uploadlvl():
    if request.method == 'POST':
        file = request.files['file']
        levelData = file.read()

        levelName = request.form.get('lvlname')
        userName = request.form.get('uploadername')

        cursor = get_db().cursor()
        cursor.execute("INSERT INTO user (user,levelName) VALUES (?,?)", (userName, levelName))
        cursor.execute("INSERT INTO level (levelData,levelName) VALUES (?,?)", (levelData, levelName))

        get_db().commit()

    return render_template('levels.html')

# get all levels
@app.route('/data')
def getLevels():
    cursor = get_db().cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("levels.html", results=results)

# download level
@app.route('/download/<download_id>')
def downloadlevel(download_id):
    cursor = get_db().cursor()
    sql = "SELECT levelData FROM level WHERE id = " + download_id
    cursor.execute(sql)
    levelDataSelected = cursor.fetchall()

    print(levelDataSelected)

    text_file = open("Output.txt", "w")
    text_file.write(str(levelDataSelected))
    text_file.close()

    return redirect('/data')

# uploading level page
@app.route('/uploadlvl')
def uploadlvl_():
    return render_template('uploadlevel.html')
    

        