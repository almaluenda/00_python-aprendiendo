from gpio import * 
from time import *

lampara = 0
puerta = 1

def main():
	pinMode(lampara, OUT)
	pinMode(puerta, IN)
	
	while True:
		#print(customRead(puerta))
		#delay(300)
		x = int(customRead(puerta)[0]) #estado de la puerta (0 es abierto)
		y = int(customRead(lampara)) #estado de la lámpara (0 es apagada)
		if x == 1:
			print("alguien ha entrado")
			if y == 0:
				customWrite(lampara,2)
			else:
				customWrite(lampara,2)
			delay(300)
		else:
			if y == 0:
				customWrite(lampara,0)
			elif y == 1:
				customWrite(lampara,1)
			else:
				customWrite(lampara,2)
			print("puerta cerrada")
			delay(300)
		
if __name__ == "__main__":
	main()