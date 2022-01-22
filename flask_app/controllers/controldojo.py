from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import ninjacls
from flask_app.models.dojo import dojocls

@app.route('/dojo')
def dojopg():
    return render_template("dojo.html")

@app.route('/ninja')
def ninjapg():
    return render_template("ninja.html")

@app.route('/dojo/show/<int:id>')
def show(id):
    data={
        "id":id
    }
    return render_template("show.html", ninja=dojocls.get_one(data))