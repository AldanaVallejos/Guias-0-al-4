#***********************************************************
# Guia de ejercitación nº2
# Fecha: 13/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 2: Dados N y M números naturales, informar su producto por sumas sucesivas.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: N, M
# Salidas: producto
# Procesos: Ingresar numero N
#           Ingresar numero M
#           Determinar que sean numeros naturales
#           Calcular su producto -> producto=
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
N=0
M=0
producto=0

N=int(input("Ingrese el primer número: "))
M=int(input("Ingrese el segundo número: "))

while M!=0:
    producto=producto+N
    M=M-1

# Salida por pantalla
print("El producto entre los dos números ingresados es {0}".format(producto))