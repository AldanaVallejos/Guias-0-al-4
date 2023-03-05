#***********************************************************
# Guia de ejercitación nº1
# Fecha: 02/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 11: Escribir un programa que le pregunte al usuario un número n
#               e imprima los primeros n números triangulares, junto 
#               con su índice. Los números triangulares se obtienen mediante
#               la suma de los números naturales desde 1 hasta n. Es decir, si se
#               piden los primeros 5 números triangulares, el programa debe imprimir:
#               1 - 1 
#               2 - 3 
#               3 - 6 
#               4 - 10 
#               5 - 15 
#
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: n
# Salidas: resultado
# Procesos: Ingresar el numero
#           Calcular los numeros triangulares
#           Mostrar por pantalla el resultado
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
n=0
resultado=0

#Ingreso de dato
print("Ingrese un número")
n= int(input())
 
#Calculo los números triangulares
resultado={}
for i in range(1,n+1):
	resultado[i]=(i*(i+1)/2)
 
for i in resultado:
    #Salida por pantalla
	print(i,resultado[i])

