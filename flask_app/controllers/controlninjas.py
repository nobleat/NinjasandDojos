from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninjacls

@app.route('/ninja')
def ninjapg():
    return render_template("ninja.html")

@app.route('/addninja',  methods=['POST'])
def addninja():
    Ninjacls.create(request.form)
    return redirect('/')

