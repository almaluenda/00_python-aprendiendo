import os

print("Conversor de divisas")
flag = False
cont = 0
dolar = 801.6
euro = 875.4
uf = 28993.7
while not flag:
    os.system('cls')
    print("\nIndique la divisa de origen")
    print("1. Dólares")
    print("2. Euro")
    print("3. UF")
    print("4. Salir")
    opcion = int(input("seleccione su opción: "))

    if opcion == 1:
        os.system('cls')
        print("\nIndique la conversión que desea realizar")
        print("1. Dólares a Euro")
        print("2. Dólares a UF")
        opt_submenu = int(input("Selecciones su opción: "))
        if opt_submenu == 1:
            dolares = float(input("Indique la cantidad de dólares que quiere convertir: "))
            print(f"{dolares} dólares en euros son: {round(dolares * 0.9156956819739548, 2)} ")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        elif opt_submenu == 2:
            dolares = float(input("Indique la cantidad de dólares que quiere convertir: "))
            print(f"{dolares} dólares en UF son: {round((dolares * dolar) / uf, 2)} ")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        else:
            print("La opción ingresada no es correcta")
            cont = cont + 1
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
            break

    if opcion == 2:
        os.system('cls')
        print("\nIndique la conversión que desea realizar")
        print("1. Euros a dólares")
        print("2. Euros a UF")
        opt_submenu = int(input("Selecciones su opción: "))
        if opt_submenu == 1:
            euros = float(input("Indique la cantidad de euros que quiere convertir: "))
            print(f"{euros} euros en dólares son: {euros * 1.092065868263473, 2}")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        elif opt_submenu == 2:
            euros = float(input("Indique la cantidad de euros que quiere convertir: "))
            print(f"{euros} euros en UF son: {round(euros * euro / uf, 2)} ")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        else:
            print("La opción ingresada no es correcta")
            cont = cont + 1
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
            break

    if opcion == 3:
        os.system('cls')
        print("\nIndique la conversión que desea realizar")
        print("1. UF a dólares")
        print("2. UF a euros")
        opt_submenu = int(input("Selecciones su opción: "))
        if opt_submenu == 1:
            ufs = float(input("Indique la cantidad de UF que quiere convertir: "))
            print(f"{ufs} UF en dólares son: {round(ufs * uf / dolar , 2)}")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        elif opt_submenu == 2:
            ufs = float(input("Indique la cantidad de UF que quiere convertir: "))
            print(f"{ufs} UF en euros son: {round(ufs * uf / euro, 2)} ")
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        else:
            print("La opción ingresada no es correcta")
            cont = cont + 1
            print("Seleccione una tecla para continuar...")
            input()
            os.system('cls')
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            break

    if opcion == 4:
        print("GRACIAS POR USAR NUESTRO SISTEMA")
        print("Seleccione una tecla para continuar...")
        input()
        os.system('cls')
        flag = True