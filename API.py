from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from Team import Team
from Championship import Championship
from Linked_List import LinkedList, Node

domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)
teams=LinkedList()
championships=LinkedList() 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("inicio.html")

@app.route("/view", methods=["GET", "POST"])
def view():
    return render_template("view.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    name = request.args.get("ChampName", " ")
    championships.head=Node(Championship(name, None, None))
    return render_template("create.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
