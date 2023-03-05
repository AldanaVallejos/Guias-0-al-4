#***********************************************************
# Guia de ejercitación nº1
# Fecha: 01/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 10: Escribir un programa que imprima todos los números
#               pares entre dos números que se le pidan al usuario.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: numero1, numero2
# Salidas: pares
# Procesos: Ingresar numero1
#           Ingresar numero2
#           Crear un bucle for
#           Mostrar los pares por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero1=0
numero2=0

#Ingreso de datos
print("Ingrese el primer número")
numero1=int(input())

print("Ingrese el segundo número")
numero2=int(input())

#Creo un bucle for
for pares in range(numero1,numero2+1):
    if pares%2==0:
       #Salida por pantalla
            print (pares)

            