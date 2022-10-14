# datos del usuario
rut = "13.444.555-4"
nombre ="José Cifuentes Riquelme"
marca = "Fiat"
modelo = "punto"


# tiempos de servicios
t_revision_km = 2
t_cambio_aceite = 1
t_frenos = 0.5
t_correas = 0.5
t_luces = 0.2
t_direccion = 0.5

# Solicitud de información al cliente
# print("Bienvenido/a")

""" # servicio de lavado
print("Servicio de lavado")
a = int(input("Desea el servicio de revisión de 1000 km \n 1. Si \n 2. No \n Ingrese su respuesta: "))

# servicio de cambio de aceite
print("\n Cambio de aceite")
b = int(input("Desea el servicio de cambio de aceite \n 1. Si \n 2. No \n Ingrese su respuesta: "))

# servicio de frenos
print("\n Mantenimiento de frenos")
c = int(input("Desea el servicio de mantenimiento de frenos \n 1. Si \n 2. No \n Ingrese su respuesta: "))
 """

# solicitud de servicios
# 1: servicio solicitado
# 2: servicio no solicitado 
a = 1
b = 1
c = 2
d = 2
e = 1
f = 1
cantidad = 0
if a == 1:
    cantidad = cantidad + 1
if b == 1:
    cantidad = cantidad + 1
print(cantidad)    
# salida en pantalla
""" print("--------------------------------------")
print("             Servicio automotriz      ")
print("--------------------------------------")
print(f"Cliente: {nombre} ")
print(f"Servicios: ")
print(f"Cantidad: ")
print("Tiempo de espera: ")
print("Estado: Terminado") """