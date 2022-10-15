#Contador de votos online

#Definimos las funciones que vamos a utilizar1
def pantalla():
    import os
    return os.system("clear")

def republicano():
    global repu
    pantalla()
    repu = repu + 1
    

def democrata():
    global demo
    pantalla()
    demo = demo + 1

def total(repu, demo):
    print(f"El total de votos republicanos a la fecha es : {repu}")
    print(f"El total de votos demócratas a la fecha es : {demo}")
    return

def salir():
    global flag
    pantalla()
    flag = True


#Realizamos una primera limpieza de pantalla
pantalla()

#Iniciamos flags y contadores en cero
flag = False
repu = 0
demo = 0

#Rutina basada en un while, sale de ella cuando Flag = True
while not flag:
    print("         *** MENU ***")
    print("=============================")
    print("[1] -> Partido Republicano")
    print("[2] -> Partido Demócrata")
    print("[3] -> Total de votos")
    print("[4] -> Salir del sistema")
    print("=============================")
    print("")
    opt = int(input("Ingrese una opción : "))

    if opt == 1: #Invoca función que permite contar un voto republicano
        republicano()

    elif opt == 2: #Invoca función que permite contar un voto republicano
        democrata()

    elif opt == 3: #Invoca función que muestra en pantalla el conteo (NOTA: Se puede seguir con el conteo / No borra los datos)
        total(repu, demo)

    else: #Invoca función que permite salir del programa
        salir()
