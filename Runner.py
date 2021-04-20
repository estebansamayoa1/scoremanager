from Team import Team 



print("Bienvenido al Score Manager")
teams=[]
x=1
while (x!=0):
    print("1.Ingresar Equipos\n2.Ver Equipos\n3.Match\n4.Salir\n")
    opcion=int(input())
    if opcion==1:
        nombre=input("Ingrese el nombre del equipo")
        size=input("Ingrese la cantidad de jugadores")
        teams.append(Team(nombre, size, 0))

    if opcion==2:
        for team in teams:
            print("----------------------------------------")
            print (f"Nombre del equipo:{team.name}\nCantidad de jugadores:{team.size}\nPuntos acumulados:{team.score}\n")

    if opcion==4:
        x=0
        exit()

    
