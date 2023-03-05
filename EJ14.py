#***********************************************************
# Guia de ejercitación nº1
# Fecha: 02/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 14: Modificar el programa anterior para que pueda generar
#               fichas de un juego que puede tener números de 0 a n
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: cantidad, continuar
# Salidas: cantidad
# Procesos: Ingreso una cantidad de fichas
#           Compruebo que sea un valor entero
#           Muestro los números por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
cantidad=0
continuar="S"

# Creo un ciclo de repetición
while continuar=="S":
    if continuar=="S":
        # Ingreso de dato
        print("Ingrese una cantidad de fichas ")
        cantidad=int(input())
        continuar="N"
    else:
        # Muestro un mensaje de error
        print("Ingrese únicamente valores enteros\n")
for n in range (cantidad+1):
    for x in range (n,cantidad+1):
        #Salida por pantalla
        print(n,x)

        