#***********************************************************
# Guia de ejercitación nº1
# Fecha: 29/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 8: Escribir una función que convierta un valor dado
#              en grados Fahrenheit a grados Celsius. Recordar que
#              la fórmula para la conversión es: F=(9/5)*C+32
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: F
# Salidas: cel
# Procesos: Ingresar grados fahrenheit
#           Calcular la conversión a grados Celcius -> (F − 32)*(5/9) = C
#           Mostrar por pantalla el resultado
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
F=0.00
cel=0.00

#Ingreso de dato
print("Ingrese los grados Fahrenheit")
F=float(input())

#Calculo la conversión
cel=(F-32)*(5/9)

#Salida por pantalla
print("En grados Celsius seria {0}".format(cel))
