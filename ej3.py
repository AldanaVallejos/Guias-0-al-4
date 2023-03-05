#***********************************************************
# Guia de ejercitación nº0
# Fecha: 26/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 3: Escribir un programa que pregunte el nombre
#              del usuario en la consola y, después de que el
#              usuario lo introduzca, muestre por pantalla la
#              cadena ¡Hola <nombre>!, donde <nombre> es le
#              nombre que el usuario haya introducido.     
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

# Ingreso de dato
print ("Introduzca su nombre")
nombre=input()

# Salida por pantalla
print ("Hola {0}".format(nombre))
