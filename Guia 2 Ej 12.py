#***********************************************************
# Guia de ejercitación nº2
# Fecha: 06/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 12: Escribir un algoritmo, que devuelva el valor
#               absoluto de cualquier valor que reciba. 
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: num
# Salidas: abs
# Procesos: Ingresar un valor cualquiera
#           Mostrar por pantalla el absoluto del número ingresado
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
num=0.00

num=float(input("Ingrese un valor: "))

# Salida por pantalla
print("El absoluto de {0}".format(num),"es: ",abs(num))