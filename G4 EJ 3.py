#***********************************************************
# Guia de ejercitación nº2
# Fecha: 15/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 3: Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD),
#              que finaliza con un Nombre = ‘FIN’, informar el nombre de la 
#              persona con mayor edad y el de la más joven.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: continuar, nombresyfechas, contador
# Salidas: mayor, menor
# Procesos: Ingresar un nombre
#           Ingresar la fecha
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
continuar="S"
nombresyfechas={}
contador=0
mayor=0
menor=0

import datetime
while continuar=="S":
    # Ingreso de dato
	nombre=input("Ingrese un nombre: ")
	if nombre=="fin" or nombre=="FIN":
		continuar="N"
	else:
		nombresyfechas[nombre]=0
        # Ingreso de dato
		f=input("Ingrese fecha de nacimiento formato (ddmmaaaa) : ")
		fecha=datetime.datetime.strptime(f, '%d%m%Y')
		if contador==0:
			fechamayor=fecha
			fechamenor=fecha
		else:
			if fecha < fechamayor:
				mayor= nombre

			if fecha > fechamenor:
				menor= nombre

		nombresyfechas[nombre]= fecha
	contador+=1

# Salida por pantalla
print("El que tiene mayor edad es: ",mayor)
print("El más joven es: ",menor)
