from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from Team import Team
from Championship import Championship
from Linked_List import LinkedList, Node

domain = "0.0.0.0:5000/"
first = True
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)
teams=LinkedList()
championships = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("inicio.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if (request.method == "POST"):
        Champname = request.form['ChampName']
        FirstTeamName = request.form['FirstTeam']
        NextTeam = request.form['NextTeam']
        if (Champname):
            teams.head = Node(Team(FirstTeamName, 0))
            next_team = Node(Team(NextTeam, 0))
            teams.insert_last(next_team)
            newChamp = Championship(Champname, teams, None)
            championships.append(newChamp)
            return redirect(url_for('view', name = Champname))
    return render_template("create.html")


@app.route("/view/<name>", methods=["GET", "POST"])
def view(name):
    if (request.method == "POST"):
        FirstTeamName = request.form['FirstTeam']
        SecondTeamName = request.form['SecondTeam']
        if (FirstTeamName != None and SecondTeamName != None):
            teams.insert_last(Node(Team(FirstTeamName, 0)))
            teams.insert_last(Node(Team(SecondTeamName, 0)))
            for champ in championships:
                if (name == champ.getChampName()):
                    champ.newChampTeam(teams)
                else:
                    raise Exception
            return render_template("view.html", Champname = name, allTeams = teams.turnDict())                   
    return render_template("view.html", Champname = name, allTeams = teams.turnDict())

@app.route("/match/<name>", methods=["GET", "POST"])
def match(name):
    if (request.method == "POST"):
        Team1 = request.form['Team1']
        Team2 = request.form['Team2']
        Goal1 = request.form['Goal1']
        Goal2 = request.form['Goal2']
        if (Team1 != None and Team2 != None and Goal1 != None and Goal2 != None):
            if (teams.ElementConfirmation(Team1) == True and teams.ElementConfirmation(Team2) == True):
                team1 = teams.getElement(Team1)
                teams.remove(team1)
                team1.setScore(Goal1)
                teams.insert_last(Node(team1))
                team2 = teams.getElement(Team2)
                teams.remove(team2)
                team2.setScore(Goal2)
                teams.insert_last(Node(team2))
        return render_template("view.html", allTeams = teams.turnDict())  
    return render_template("match.html", name = name)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
