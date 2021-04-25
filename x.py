from Team import Team
from Linked_List import Node, LinkedList
from Championship import Championship

count = 1
team_number = 1
teams = LinkedList()
championships=[]
stop = True
while (stop):
    champName = input("Ingrese el nombre del torneo: ")
    nombre=input("Ingrese el nombre del equipo numero 1: ")
    teams.head = Node(Team(nombre, 0))

    while (count != 3):
        team_number += 1
        nombre=input(f"Ingrese el nombre del equipo numero {team_number}: ")
        next_team = Node(Team(nombre, 0))
        teams.insert_last(next_team)
        count = count + 1
    stop = False

championships.append(Championship(champName, teams, None))

brasil = "brasil"
print(teams.ElementConfirmation(brasil))
name = "La Fafiliga"

FirstTeamName = "rusia"
SecondTeamName = "guatemala"
Goal1 = 3
Goal2 = 2
if (FirstTeamName and SecondTeamName):
    teams.insert_last(Node(Team(FirstTeamName, 0)))
    teams.insert_last(Node(Team(SecondTeamName, 0)))
    for champ in championships:
        if (name == champ.getChampName()):
            champ.newChampTeam(teams)
            team1 = teams.getElement(FirstTeamName)
            teams.remove(team1)
            team1.setScore(Goal1)
            teams.insert_last(Node(team1))
            team2 = teams.getElement(SecondTeamName)
            teams.remove(team2)
            team2.setScore(Goal2)
            teams.insert_last(Node(team2))
        else:
            raise Exception

TheTeams = championships[0].getTeams()

dic = TheTeams.turnDict()
print(dic)

#while (stop):
    #nombre=input("Ingrese el nombre del primer torneo: ")
    #championships.head = Node(Championship(nombre, None, None))

    #while (count != 3):
        #team_number += 1
        #nombre=input(f"Ingrese el nombre del equipo numero {team_number}: ")
        #next_champ = Node(Championship(nombre, None, None))
        #teams.insert_last(next_champ)
        #count = count + 1
        #break

#for champ in championships:
    #print(champ)
