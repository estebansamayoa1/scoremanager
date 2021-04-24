from Team import Team
from Linked_List import Node, LinkedList
from Championship import Championship

count = 1
team_number = 1
teams = LinkedList()
championships=LinkedList()
stop = True
while (stop):
    nombre=input("Ingrese el nombre del equipo numero 1: ")
    teams.head = Node(Team(nombre, 0))

    while (count != 3):
        team_number += 1
        nombre=input(f"Ingrese el nombre del equipo numero {team_number}: ")
        next_team = Node(Team(nombre, 0))
        teams.insert_last(next_team)
        count = count + 1
    stop = False

for team in teams:
    print(team)

while (stop):
    nombre=input("Ingrese el nombre del primer torneo: ")
    championships.head = Node(Championship(nombre, None, None))

    while (count != 3):
        team_number += 1
        nombre=input(f"Ingrese el nombre del equipo numero {team_number}: ")
        next_champ = Node(Championship(nombre, None, None))
        teams.insert_last(next_champ)
        count = count + 1
        break

for champ in championships:
    print(champ)
