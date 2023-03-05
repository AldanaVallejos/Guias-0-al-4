#***********************************************************
# Guia de ejercitación nº2
# Fecha: 06/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 11: Escribir un algoritmo que resuelvan los siguientes problemas:
#               a) Dado un número entero n, indicar si es par o no.
#               b) Dado un número entero n, indicar si es primo o no. 
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: numero, division, v
# Salidas: par, impar, primo, no primo
# Procesos: a) Ingresar un numero entero
#           Determinar si es par o no -> n%2
#           Mostrar por pantalla
#           b) Ingresar un numero entero
#           Determinar si es primo o no -> def es_primo(num, n=2)
#           Mostrar por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero=0
division=0.00
v=0

# Ingreso de dato
numero=int(input("Ingrese un número entero: "))

# a) ¿Es par o impar?
division=numero%2

if division==0:
    print("Es par")
else:
    print("Es impar")

# b) ¿Es primo o no?

# Ingreso de dato
v=int(input("Ingrese el numero: "))

def es_primo(num, n=2):
    if n >= num:
      # Salida por pantalla
        return"Es primo"
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
      # Salida por pantalla
        return"No es primo"

print(es_primo(v))