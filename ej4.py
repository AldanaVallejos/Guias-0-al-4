#***********************************************************
# Guia de ejercitación nº0
# Fecha: 26/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: Escribi un programa que pregunte el nombre
#              del usuario en la consola y después de que
#              el usuario lo introduzca muestre por pantalla
#              “<nombre> tiene <n> letras”, donde <nombre> es
#              el nombre de usuario en mayúsculas y <n> es el
#              número de letras que tiene el nombre.  
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: nombre
# Salidas: nombre
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nombre=""

#Ingreso de dato
print("¿Cuál es su nombre?")
nombre=input()

#Salida por pantalla
print((nombre),"tiene",(len(nombre)),"letras.")
