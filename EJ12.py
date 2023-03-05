#***********************************************************
# Guia de ejercitación nº1
# Fecha: 02/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 12: Escribir un programa que tome una cantidad n de valores
#               ingresados por el usuario, a cada uno le calcule el factorial
#               (lo realizado en el ejercicio 1.4) e imprima el resultado
#               junto con el número de orden correspondiente.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: cantidad, num, factorial, continuar
# Salidas: cantidad, num, factorial
# Procesos: Ingreso la cantidad de numeros a calcular
#           Identifico si son números enteros
#           Ingreso los numeros
#           Identifico si son números enteros
#           Calculo los factoriales
#           Muestro por pantalla la cantidad, el numero y su factorial
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
cantidad=0
num=0
continuar="S"
factorial=0

#Creo un ciclo de repetición
while continuar=="S":
    if continuar=="S":
        #Ingreso de dato
        print("Ingrese una cantidad de números ")
        cantidad=int(input())
        continuar="N"
    else:
        #Muestro un mensaje de error
        print("Ingrese solo valores numéricos enteros\n")

for n in range(1,cantidad+1):
    continuar="S"
    while continuar=="S":
        if continuar=="S":
            #Ingreso de dato
            print("Ingrese un número para calcular su factorial: ")
            num=int(input())
            continuar="N"
        else:
            #Muestro mensaje de error
            print("Ingrese solo valores numéricos enteros\n")
    #Calculo el factorial
    factorial = 1
    for x in range(2,num+1):
        factorial *= x
    #Salida por pantalla
    print(n,num,factorial)

