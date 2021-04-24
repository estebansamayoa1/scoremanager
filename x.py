from Team import Team
from Linked_List import Node, LinkedList

count = 1
team_number = 1
teams = LinkedList()
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

        


