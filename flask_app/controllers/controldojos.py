from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojocls

@app.route('/')
def reroute():
    return redirect('/dojo')

@app.route('/dojo')
def dojopg():
    all_dojos=Dojocls.get_all()
    return render_template("dojo.html", all_dojos=all_dojos)

@app.route('/adddojo',  methods=['POST'])
def adddojo():
    Dojocls.create(request.form)
    return redirect('/dojo')

@app.route('/dojo/<int:id>')
def show(id):
    data={
        "id":id
    }
    return render_template("show.html", dojo=Dojocls.get_one(data))

