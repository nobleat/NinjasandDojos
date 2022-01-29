from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninjacls
from flask_app.models.dojo import Dojocls

@app.route('/ninja')
def ninjapg():
    return render_template("ninja.html", dojos=Dojocls.get_all())
    # dojos.Dojocls.get_all())

@app.route('/addninja',  methods=['POST'])
def addninja():
    # ninja.
    Ninjacls.create(request.form)
    return redirect('/')

