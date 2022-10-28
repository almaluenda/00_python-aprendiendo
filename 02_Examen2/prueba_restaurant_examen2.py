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
    opt_menu = int(input("Ingrese su opción: "))
     
    if opt_menu == 1:
        print("Usted eligio Sashimi de Chef")
        cant_1 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_1 * sashimichef
    elif opt_menu == 2:
        print("Usted eligio Spicy Roll")
        nivel2 = int(input("Que nivel de picante desea [Elija 1, 2 o 3 :]"))
        cant_2 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_2 * rollspicy
    elif opt_menu == 3:
        print("Usted eligio Vegan Roll")
        nivel3 = int(input("Que nivel de picante desea [Elija 1, 2 o 3 :]"))
        cant_3 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_3 * veganroll
    elif opt_menu == 4:
        print("Usted eligio Chicken Teriyaki")
        cant_4 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_4 * chicken
    elif opt_menu == 5:
        print("Usted eligio Pulpo roll")
        cant_5 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_5 * pulpo
    elif opt_menu == 6:
        print("Usted eligio Wasabi roll")
        nivel6 = int(input("Que nivel de picante desea [Elija 1, 2 o 3 :]"))
        cant_6 = int(input("Ingrese Cantidad : "))
        pedido = pedido + cant_6 * wasabi
    
    elif opt_menu == 7:
            print()
            print (f"Su pedido total sin descuento es : {pedido}\n ")
            print (f"Su pedido con descuento = {valor_desc(pedido)}\n")
        
    elif opt_menu == 8:
        print("Gracias")
        borrar()
        menu_flag = True
    else:
        print("Ingrese una opcion valida") 