#***********************************************************
# Guia de ejercitación nº2
# Fecha: 13/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 1: Informar los primeros 100 números naturales y su sumatoria.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: 
# Salidas: numeros, suma
# Procesos: Muestro los 100 numeros naturales
#           Calcular la sumatoria entre ellos
#           Mostrar la sumatoria en pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numeros=1
suma=0

# Salida por pantalla
print("Los primeros 100 números naturales")

while numeros>0 and numeros<=100:
    # Salida por pantalla
    print(numeros, end=" ")
    # Contador
    numeros=numeros+1
    

# Calculo la sumatoria
suma=(((1+100))/2)*100

# Salida por pantalla
print(end="\n")
print("La sumatoria entre los primeros 100 números naturales es: {0}".format(suma))
