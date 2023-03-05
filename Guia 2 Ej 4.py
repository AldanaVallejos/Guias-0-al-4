#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: A partir de un valor entero ingresado por teclado, se pide informar:
#              a)	La quinta parte de dicho valor
#              b)	El resto de la división por 5
#              c)	La séptima parte del resultado del punto a)

#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: cantidad
# Salidas: division
# Procesos: Ingresar el valor
#           Calcular la quinta parte del valor -> division=cantidad/5
#           Calcular el resto de la división por 5 -> cantidad%5
#           Calcular la séptima parte del resultado del punto a) -> division/7
#           Mostrar los resultados por teclado
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
cantidad=0
division=0
resto=0
parte7=0

# Ingreso de dato
cantidad=int(input("Ingrese el número: "))

# Calcular la quinta parte
division=cantidad/5

# Calcular el resto de la división por 5
resto=cantidad%5

# Calcular la séptima parte
parte7=division/7

# Salida por pantalla
print("a) La quinta parte de {0}".format(cantidad),"es: {0}".format(division))
print("b) El resto de la división por 5 es: {0}".format(resto))
print("c) La séptima parte del resultado del punto a) es: {0}".format(parte7))