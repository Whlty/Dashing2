from application import app
from application import models
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


@app.route('/upload',methods=["GET","Post"])
def upload():
    filename = request.form.get("file")
    print(filename)

    cursor = get_db().cursor()
    cursor.execute("INSERT into user (levelName) VALUES (?)")
    get_db().commit()
    return redirect("/")


@app.route('/data')
def getLevels():
    #stats display for one user
    cursor = get_db().cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("levels.html", results=results)

@app.route('search',methods=["GET","Post"])
def search():


@app.route('/download')
def downloadOnline()
    id = request.form.get("levelname")
    cursor = get_db().cursor()
    sql = "SELECT level FROM user WHERE id="

        