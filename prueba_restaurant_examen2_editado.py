#Restaurante de Sushi Cepeda, Maluenda, Olea
import os 

menu_flag = False 

def menu():
    print("SUSHI")
    print("*******MENÚ DE OPCIONES*******")
    print("="*20)
    print("[1]-> Sashimi del Chef ")
    print("[2]-> Roll spicy extreme (Picante) ")
    print("[3]-> Vegan Roll (opcional Picante) ")
    print("[4]-> Chicken Teriyaki " )
    print("[5]-> Pulpo roll ")
    print("[6]-> Wasabi roll (Picante) ")
    print("[7]-> Totalización y Cierre de caja ")
    print("[8]-> Salir")

def borrar():
  os.system('cls')


def valor_desc(subtotal):
    if subtotal >= 15000:
        valor_desc = subtotal * 0.9
    else:
        valor_desc = subtotal
    return valor_desc

def validacion(cadena):
    if cadena is "1":
        aux = 1
    elif cadena is "2":
        aux = 2
    elif cadena is "3":
        aux = 3
    elif cadena is "4":
        aux = 4
    elif cadena is "5":
        aux = 5
    elif cadena is "6":
        aux = 6
    elif cadena is "7":
        aux = 7
    elif cadena is "8":
        aux = 8
    else:
        aux = 0
    return aux


# precio servicios
sashimichef = 8990
rollspicy = 5990
veganroll = 4950
chicken = 6990
pulpo = 7990
wasabi = 4990

pedido = 0

borrar()

while not menu_flag:
    
    menu()
    opt_menu = input("Ingrese su opción: ")
    
    opcion = validacion(opt_menu)
     
    if opcion == 1:
        cant_1 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_1 * sashimichef
        borrar()
        print("*"*50)
        print("Usted eligio Sashimi de Chef")
        print("*"*50)

    elif opcion == 2:
        nivel2 = int(input("Que nivel de picante desea [Elija 1, 2 o 3 :]"))
        cant_2 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_2 * rollspicy
        borrar()
        print("*"*50)
        print("Usted eligio Spicy Roll")
        print("*"*50)

    elif opcion == 3:
        nivel3 = int(input("Que nivel de picante desea [Elija 1, 2 o 3 :]"))
        cant_3 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_3 * veganroll
        borrar()
        print("*"*50)
        print("Usted eligio Vegan Roll")
        print("*"*50)

    elif opcion == 4:
        cant_4 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_4 * chicken
        borrar()
        print("*"*50)
        print("Usted eligio Chicken Teriyaki")
        print("*"*50)

    elif opcion == 5:
        cant_5 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_5 * pulpo
        borrar()
        print("*"*50)
        print("Usted eligio Pulpo roll")
        print("*"*50)

    elif opcion == 6:
        nivel6 = int(input("Que nivel de picante desea [Elija 1, 2 o 3 :]"))
        cant_6 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_6 * wasabi
        borrar()
        print("*"*50)
        print("Usted eligio Wasabi roll")
        print("*"*50)
    
    elif opcion == 7:
        borrar()
        print("*"*50)
        print()
        print (f"Su pedido total sin descuento es : $ {pedido}\n ")
        print (f"Su pedido con descuento : $ {valor_desc(pedido)}\n")
        print("*"*50)
        pedido = 0
        
    elif opcion == 8:
        borrar()
        print("*"*50)
        print("*"*50)
        print("*"*21+"GRACIAS"+"*"*22)
        print("*"*50)
        print("*"*50)
        menu_flag = True

    elif opcion == 0:
        borrar()
        print("*"*50)
        print("Ingrese una opcion valida")
        print("*"*50)

    else:
        borrar()
        print("*"*50)
        print("Ingrese una opcion valida")
        print("*"*50)