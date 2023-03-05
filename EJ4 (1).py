#***********************************************************
# Guia de ejercitación nº1
# Fecha: 29/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su factorial.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: n
# Salidas: factorial
# Procesos: Ingresar un numero entero 
#           Calcular su factorial
#           Mostrar por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
n=0
factorial=0

#Ingreso de dato
print("Ingrese un número entero")
n=int(input())

#Salida por pantalla
from math import factorial
print("El factorial es", (factorial(n)))

