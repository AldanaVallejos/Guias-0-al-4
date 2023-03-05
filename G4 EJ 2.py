#***********************************************************
# Guia de ejercitación nº2
# Fecha: 15/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 2: Dados N valores informar el mayor, el menor
#              y en que posición del conjunto fueron ingresados.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: continuar, nro, numeros, contador
# Salidas: nromayor
# Procesos:   Ingresar numeros
#             calcular el mayor
#             calcular el menor
#             Mostrarlos por pantalla con posicion
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nromayor=0
continuar="S"
contador=0
nro=0
numeros=[]

while continuar=="S":
    # Ingreso de dato
	nro=(int(input("Ingrese un numero: ")))
	if nro==0:
		continuar="N"
	else:
		numeros.append(nro)
	contador=contador+1

for i in numeros:
	if i > nromayor:
        # Calculo el mayor
		nromayor=i
		posnromayor= numeros.index(i)

minimo=numeros[0]
for a in numeros:
	if a < minimo:
        # Calculo el menor
		minimo = a
		posnromenos= numeros.index(a)

# Salida por pantalla
print("El numero mayor es %d con posicion en %d" %(nromayor,posnromayor+1))
print("El numero menor es %d con posicion en %d" %(minimo, posnromenos+1))