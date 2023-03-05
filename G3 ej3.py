#***********************************************************
# Guia de ejercitación nº2
# Fecha: 13/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 3: Dados 50 números enteros, informar el promedio 
#              de los mayores que 100 y la suma de los menores que –10.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: numeros
# Salidas: promedio, suma
# Procesos: Ingresar los numeros hasta 50
#           calcular el promedio
#           calcular la suma
#           Mostrar el promedio y la suma por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numeros=1
promedio=0
suma=0
naturales=0
rpromedio=0

for i in range(50):
    # Salida por pantalla
    naturales=int(input(f"Ingrese el valor {numeros} de los 50 numeros a ingresar: "))
    numeros+=1
    if naturales>=100:
        # Calculo el promedio
        promedio=naturales%100
        rpromedio+=naturales
    elif naturales<=-10:
        # Calculo la suma
        suma+=naturales

# Salida por pantalla 
print (f"El promedio de los numeros mayores a 100 es: {rpromedio}")
print (f"La suma de los numeros menores a -10 es: {suma}")