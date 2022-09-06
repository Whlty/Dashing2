from application import app
from application import models
from flask import Flask, render_template, request, redirect
import os


@app.route('/')
def datastuff():
    return render_template("editor.html")


@app.route('/upload',methods=["GET","Post"])
def upload():
     for file in request.files.getlist("file"):
        filename = file.filename
        destination = os.path.join("static/files", filename)
        file.save(destination)

        user = User()
        
        user.level = destination
        db.session.add()
        return redirect("/")

        