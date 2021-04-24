from Team import Team 
from Linked_List import Node, LinkedList

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("BIENVENIDO AL SCORE MANAGER")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
teams = LinkedList()
x=1
while (x!=0):
    print("\n1.Ingresar Equipos\n2.Ver Equipos\n3.Match\n4.Salir\n")
    opcion=int(input())
    if opcion==1:
        nombre=input("Ingrese el nombre del equipo: ")
        size=input("Ingrese la cantidad de jugadores: ")
        teams.append(Team(nombre, size, 0))

    if opcion==2:
        print("LOS EQUIPOS INSCRITOS AL TORNEO SON: ")
        for team in teams:
            print("----------------------------------------")
            print (f"Nombre del Equipo: {team.name}\nCantidad de Jugadores: {team.size}\nPuntos Acumulados: {team.score}\n")

    if opcion==3:
        primero=input("Ingrese el nombre del primer equipo que jugara: \n")
        segundo=input("Ingrese el nombre del contrincante: \n")
        contrincantes=[]
        print("PARTIDO EN JUEGO: \n")
        for team in teams:
            if primero==team.name:
                contrincantes.append(team)
                print("----------------------------------------")
                print (f"Nombre del Equipo: {team.name}\nCantidad de Jugadores: {team.size}\nPuntos Acumulados: {team.score}\n")
            elif segundo==team.name:
                contrincantes.append(team)
                print("----------------------------------------")
                print (f"Nombre del Equipo: {team.name}\nCantidad de Jugadores: {team.size}\nPuntos Acumulados: {team.score}\n")
            else:
                print ("El equipo no se encuentra en el torneo.\n")
            op=int(input("1.Agregar un punto\n2.Terminar el partido\n"))
            if op==1:
                i=1
                for team in contrincantes:
                    print (f"{i}.{team.name}\n")
                    i+=1
        
        
    if opcion==4:
        x=0
        exit()

    
