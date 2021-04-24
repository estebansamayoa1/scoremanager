from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("inicio.html")

@app.route("/view", methods=["GET", "POST"])
def view():
    return render_template("view.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    championship = request.args.get("ChampName", " ")
    
    return render_template("create.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)