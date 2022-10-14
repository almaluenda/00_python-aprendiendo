#vamos a realizar programa para ventas online
print("EDUCATE-ONLINE VENTA DE CURSOS")
import os
os.system("cls")
flag_salir = False

valor_prog=250000
valor_bases=310000
valor_robot=280000
cuenta = 0
flag_prog=0
flag_bases=0
flag_robot=0
cupon = False

while not flag_salir:
    print("Valores semestrales de los cursos:")
    print("1. Progamación : $250.000")
    print("2. Bases de datos : $310.000")
    print("3. Robótica : 280.000")
    print("4. Salir/Finalizar")
    curso = int(input("Seleccione el curso al que se desea inscribir: "))

    if curso == 1:
        os.system("cls")
        if flag_prog==0:
            flag_prog=1
            nombre=input("\nIngrese nombre del alumno : ")
            rut=input("Ingrese rut del alumno : ")
            tiene_cupon = input("Ingrese cupón de descuento (presione cualquier tecla para omitir) : ")
            if tiene_cupon != "EDUCATE-ONLINE":
                print(" > > sin cupón de descuento o cupón erróneo < < ")
                cuenta=cuenta+valor_prog
            else:
                print(" > > cupón de descuento ingresado correctamente < < ")
                cuenta=cuenta+valor_prog*0.8
            print("******************************************")
            print("Usted ha inscrito el curso PROGRAMACIÓN")
            print("******************************************")
            print("¿Desea seguir inscribiendo cursos?")
            print("1. Sí / 2. No")
            seguir = int(input("Ingrese su respuesta : "))
            os.system("cls")
            if seguir == 2:
                #flag_salir=True
                break

        else:
            print("******************************************")
            print("Ya ha inscrito este curso")
            print("******************************************")
            #break
    elif curso == 2:
        os.system("cls")
        if flag_bases==0:
            flag_bases=1
            nombre=input("\nIngrese nombre del alumno : ")
            rut=input("Ingrese rut del alumno : ")
            tiene_cupon = input("Ingrese cupón de descuento (presione cualquier tecla para omitir) : ")
            if tiene_cupon != "EDUCATE-ONLINE":
                print(" > > sin cupón de descuento o cupón erróneo < < ")
                cuenta=cuenta+valor_bases
            else:
                print(" > > cupón de descuento ingresado correctamente < < ")
                cuenta=cuenta+valor_bases*0.8
            print("******************************************")
            print("Usted ha inscrito el curso BASES DE DATOS")
            print("******************************************")
            print("¿Desea seguir inscribiendo cursos?")
            print("1. Sí / 2. No")
            seguir = int(input("Ingrese su respuesta : "))
            os.system("cls")
            if seguir ==2:
                #flag_salir=True
                break
        else:
            print("******************************************")
            print("Ya ha inscrito este curso")
            print("******************************************")
            #break

    elif curso == 3:
        os.system("cls")
        if flag_robot==0:
            flag_robot=1
            nombre=input("\nIngrese nombre del alumno : ")
            rut=input("Ingrese rut del alumno : ")
            tiene_cupon = input("Ingrese cupón de descuento (presione cualquier tecla para omitir) : ")
            if tiene_cupon != "EDUCATE-ONLINE":
                print(" > > sin cupón de descuento o cupón erróneo < < ")
                cuenta=cuenta+valor_robot
            else:
                print(" > > cupón de descuento ingresado correctamente < < ")
                cuenta=cuenta+valor_robot*0.8
            print("******************************************")
            print("Usted ha inscrito el curso ROBÓTICA")
            print("******************************************")
            print("¿Desea seguir inscribiendo cursos?")
            print("1. Sí / 2. No")
            seguir = int(input("Ingrese su respuesta : "))
            os.system("cls")
            if seguir ==2:
                #flag_salir=True
                break
        else:
            print("******************************************")
            print("Ya ha inscrito este curso")
            print("******************************************")
            #break

    elif curso == 4:
        flag_salir = True

print("******************************************")
print(f"Nombre : {nombre} // RUT : {rut}")
print(f"Total de cursos comprados sin descuento: {flag_prog+flag_bases+flag_robot}")
#print(f"Total de cursos comprados con descuento:{}")
print(f"Valor de cursos comprados sin descuento$: {flag_prog*valor_prog + flag_bases*valor_bases + flag_robot*valor_robot}")
print(f"Valor de cursos comprados con descuento$: {cuenta}")
print("******************************************")