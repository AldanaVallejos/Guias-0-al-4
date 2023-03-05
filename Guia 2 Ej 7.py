#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 7: Dado un triángulo representado por sus lados L1, L2, L3,
#              determinar e imprimir una leyenda según sea: equilátero, isósceles o escálenos.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: L1, L2, L3
# Salidas: isósceles, equilátero, escaleno
# Procesos: Ingresar el primer lado
#           Ingresar el segundo lado
#           Ingresar el tercer lado
#           Determino si: L1=L2=L2 -> equilátero
#                         L1=L2!=L3 -> isósceles
#                         L1!=L2!=L3 -> escaleno
#           Muestro el resultado por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
L1=0
L2=0
L3=0

# Ingrese los lados
L1=int(input("Ingrese el primer lado: "))
L2=int(input("Ingrese el segundo lado: "))
L3=int(input("Ingrese el tercer lado: "))

#Determino la opcion elegida mediante condicionales anidados
if L1==L2!=L3:
		print("Es un triángulo isósceles")
else:
		if L1!=L2!=L3:
			print("Es un triángulo escaleno")
		else:
			if L1==L2==L3:
				print("Es un triángulo equilátero")
			else:
				print("Valor inválido")