#***********************************************************
# Guia de ejercitación nº1
# Fecha: 29/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 6:  Escribir un programa que le pida una palabra al usuario,
#               para luego imprimirla 1000 veces, en una única línea, 
#               con espacios intermedios. Ayuda: Investigar acerca del parámetro 
#               end de la función print
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: palabra, continuar
# Salidas: palabra
# Procesos: Ingresar una palabra
#           Mostrar la repetición de esa palabra en una linea con espacios intermedios
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
palabra=""
contador=1

#Ingreso de dato
print("Escriba una palabra")
palabra=input()

while (contador)<1000:
    print((palabra),end=" ")
    contador=contador+1

    