from application import app
from flask import Flask, render_template

@app.route('/')
def datastuff():
    return render_template("editor.html")