from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import dojocls

@app.route('/dojo')
def index():
    return render_template("dojo.html")