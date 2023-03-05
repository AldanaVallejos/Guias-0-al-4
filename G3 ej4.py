#***********************************************************
# Guia de ejercitación nº2
# Fecha: 15/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: En un torneo de fútbol participan K equipos. El torneo se juega
#              con el sistema de todos contra todos. Por cada partido disputado
#              por un equipo se dispone de la siguiente información :
#              a)	Nro. de equipo,
#              b)	Código del resultado ('P'= Perdido, 'E'= Empatado, 'G'= Ganado).
#              Se arma un lote de datos con todos los resultados del torneo, agrupados por Nro. de equipo.
#              Desarrollar el programa que imprima:
#              1) Por cada equipo, su número y el puntaje total que obtuvo (suma 3 si gana, y 1 si empata).
#              2) Nro. de equipo que totalizó la menor cantidad de puntos. (hay solo uno)
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
K=-1
continuar="S"
nro=0
resultado=""
puntaje=0
puntajetotal=0
puntajeganados=0
puntajeempatados=0
minimo=10000000000

while K<0: #Validaciones
	try:
		K=int(input("Ingrese la cantidad de equipos: ")) #Ingreso de dato
		if K<0:
			print("Error. Ingrese número mayor a 0")
		else:
			break
	except ValueError:
		print("Error. Tenés que ingresar una cantidad de equipos")

while K>0:
	K=K-1
	nro=int(input("Ingrese el numero de equipo: ")) #Ingreso de dato
	resultado=input("Ingrese el resultado (G E o P): ") #Ingreso de dato

	if resultado=="G": #Caso de resultado=ganado
		puntajeganados=puntajeganados+3
		print("El puntaje del equipo {0} es {1}".format(nro,puntajeganados)) #Salida por pantalla
	else:
		if resultado=="E": #Caso de resultado=empatado
			puntajeempatados=puntajeempatados+1
			print("El puntaje del equipo {0} es {1}".format(nro,puntajeempatados)) #Salida por pantalla
		else:
			if resultado=="P": #Caso de resultado=perdido
				puntaje=0
				print("El puntaje del equipo {0} es 0".format(nro)) #Salida por pantalla
			else:
				print("ERROR - Ingrese un resultado válido")
				resultado=input("Ingrese el resultado: ")
	
	if nro>=0:
		if nro<minimo:
			minimo=nro

	if K>0:
		if puntajetotal<minimo:
			 minimo=puntajetotal

#Salidas por pantalla
print("La cantidad de equipos ingresados fueron: {0}".format(nro, puntajetotal))
print("El equipo que totalizó la menor cantidad de puntos fue el: {0}".format(nro))