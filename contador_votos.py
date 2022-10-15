#Contador de votos online
from sys import flags


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

pantalla()
flag = False
repu = 0
demo = 0

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

    if opt == 1:
        republicano()

    elif opt == 2:
        democrata()

    elif opt == 3:
        total(repu, demo)

    else:
        salir()
