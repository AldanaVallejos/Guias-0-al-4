#***********************************************************
# Guia de ejercitación nº1
# Fecha: 28/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 1: Escribir un programa que pregunte al usuario:
#              a) su nombre, y luego lo salude. b) dos números, y
#              luego muestre el producto.  
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: nombre, numero1, numero2
# Salidas: nombre, producto
# Procesos: Ingresar nombre
#           Ingresar numero1
#           Ingresar numero2
#           Calcular el producto entre los dos numeros -> producto=numero1*numero2
#           Mostrar producto
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nombre=""
numero1=0.00
numero2=0.00
producto=0.00

#Ingreso de dato
print("¿Cuál es su nombre?")
nombre=input()

#Salida por pantalla
print("Hola {0}".format(nombre))

#Ingreso de dato
print("Ingrese dos números")
numero1=float(input())
numero2=float(input())

#Calculo el producto entre los dos numeros ingresados
producto=numero1*numero2

#Salida por pantalla
print("El producto entre los dos números ingresados es {0} ".format(producto))
