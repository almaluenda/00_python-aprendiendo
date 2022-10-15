print('VOTATRON 1.0')

cont = 0
cont_republicano = 0
cont_democratico = 0
cont_nulo = 0
import os


print("Bienvenido a tu voto digital, \n a continuacion selecciona la opcion del 1 al 4 ")
flag = False
while not flag:
 print("1. Voto por Republicano")
 print("2. Voto por Demotratico")
 print("3. Voto Nulo")
 print("4. Salir del sistema")
 opt_main_menu = int(input("¡Ingresa tu eleccion!: "))
 if opt_main_menu == 1:
    cont_republicano = cont_republicano + 1
 if opt_main_menu == 2:
    cont_democratico = cont_democratico + 1
 if opt_main_menu == 3:
    cont_nulo = cont_nulo + 1
 if opt_main_menu == 4:
    flag = True
    os.system("clear")