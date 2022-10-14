#vamos a realizar una calculadora para convertir divisas
print("Conversor de divisas")
flag = False
cont = 0
dolar = 801.6
euro = 875.4
uf = 28993.7
while not flag:
    print("\nIndique la divisa de origen")
    print("1. Dólares")
    print("2. Euro")
    print("3. UF")
    print("4. Salir")
    opcionA = int(input("seleccione su opción: "))

    if opcionA == 1:
        print("\nIndique la conversión que desea realizar")
        print("1. Dólares a Euro")
        print("2. Dólares a UF")
        opcionB = int(input("Selecciones su opción: "))
        if opcionB == 1:
            dolares = float(input("Indique la cantidad de dólares que quiere convertir: "))
            print(f"{dolares} dólares en euros son: {round(dolares * 0.9156956819739548, 2)} ")
        elif opcionB == 2:
            dolares = float(input("Indique la cantidad de dólares que quiere convertir: "))
            print(f"{dolares} dólares en UF son: {round((dolares * dolar) / uf), 2} ")
        else:
            print("La opción ingresada no es correcta")
            cont = cont + 1
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            break

    if opcionA == 2:
        print("\nIndique la conversión que desea realizar")
        print("1. Euros a dólares")
        print("2. Euros a UF")
        opcionB = int(input("Selecciones su opción: "))
        if opcionB == 1:
            euros = float(input("Indique la cantidad de euros que quiere convertir: "))
            print(f"{euros} euros en dólares son: {round( euros * 1.092065868263473, 2)}")
        elif opcionB == 2:
            euros = float(input("Indique la cantidad de euros que quiere convertir: "))
            print(f"{euros} euros en UF son: {euros * euro / uf} ")
        else:
            print("La opción ingresada no es correcta")
            cont = cont + 1
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            break

    if opcionA == 3:
        print("\nIndique la conversión que desea realizar")
        print("1. UF a dólares")
        print("2. UF a euros")
        opcionB = int(input("Selecciones su opción: "))
        if opcionB == 1:
            ufs = float(input("Indique la cantidad de UF que quiere convertir: "))
            print(f"{ufs} UF en dólares son: {round(ufs * uf / dolar , 2)}")
        elif opcionB == 2:
            ufs = float(input("Indique la cantidad de UF que quiere convertir: "))
            print(f"{ufs} UF en euros son: {round(ufs * uf / euro, 2)} ")
        else:
            print("La opción ingresada no es correcta")
        cont = cont + 1
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            break

    if opcionA == 4:
        flag = True