#***********************************************************
# Guia de ejercitación nº4
# Fecha: 24/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 6: Dada una serie de M pares {color, número} que corresponden a los tiros de una ruleta. Se pide informar:
#              a)	cuántas veces salió el número cero y el número anterior a cada cero
#              b)	cuántas  veces seguidas llegó a repetirse el color negro
#              c)	cuántas  veces seguidas llegó a repetirse el mismo número y cuál fue
#              d)	el mayor número de veces seguidas que salieron alternados el rojo y el negro
#              e)	el mayor número de veces seguidas que se negó la segunda docenas
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables

##Negro son los numeros cuya suma de digitos es par (Las excepciones son
##el 10 y el 28 ambos negros)
##Rojo es numero impar
##La ruleta se divide en 3 docenas: del 0 al 12, 12 al 24 y del 24 al 36.
##Declaracion de variables
cantidad_ceros=0
cantidad_negro=0
veces_almacenadas=0
veces_seguidas=0
repeticiones_almacenadas=0
veces_alternadas=0
cantidad_rojos=0
numero_repetido=0
repeticiones=0
negardocena=0
veces_alter_almacenadas=0
docena_almacenada=0
par=0

import random
from typing import ValuesView
try: #Validaciones
    tiradas=int(input("Ingrese cuantas veces desea tirar la ruleta: ")) #Ingreso de dato
except ValueError:
    print("Error. Ingrese un número")
    tiradas=int(input("Ingrese cuantas veces desea tirar la ruleta: "))
if tiradas < 0 or tiradas>36: #Validación
    print("Error. Tiene que ingresar un valor mayor a 0 y menor que 36")
    tiradas=int(input("Ingrese cuantas veces desea tirar la ruleta: "))
else:
    for i in range(0,tiradas):
        tirada = random.randrange(36)
    #Formula de pares
        tiradapar = tirada
        while tiradapar != 0:
            par+=tiradapar%10
            tiradapar=tiradapar//10
        if tirada == 0: #Veces que salió el numero cero y el numero anterior a cada cero
            cantidad_ceros+=1
            print("El numero anterior al cero es:{0} y se repitio {1} ceros".format(numero_anterior,cantidad_ceros)) #Salida por pantalla
        else:
            numero_anterior = tirada
        if tirada == 10 or tirada == 28: #Veces seguidas que se llegó a repetir el color negro
            cantidad_negro+=1
            veces_seguidas+=1
        else:
            if par%2 == 0:
                cantidad_negro+=1
                veces_seguidas+=1
            else:
                cantidad_rojos+=1
                if veces_seguidas > 1:
                    if veces_seguidas > veces_almacenadas:
                        veces_almacenadas = veces_seguidas
                    else:
                        veces_alternadas+=1
                        if veces_alternadas > veces_alter_almacenadas:
                            veces_alter_almacenadas = veces_alternadas
                        veces_seguidas = 0

        if tirada == numero_repetido: #Veces seguidas que llegó a repetirse el mismo numero
            repeticiones+=1
            print("Se repitió el número: {0}".format(numero_repetido)) #Salida por pantalla
        else:
            if repeticiones > repeticiones_almacenadas:
                repeticiones_almacenadas = repeticiones
            repeticiones = 0
        numero_repetido = tirada
        if tirada < 12 or tirada > 24: #Veces seguidas que se negó la segunda docena de la ruleta
            negardocena+=1
        else:
            if negardocena > docena_almacenada:
                docena_almacenada = negardocena
            negardocena=0

#Salidas por pantalla
print("La cantidad de veces seguidas que se repitio el mismo numero fueron: {0}".format(repeticiones_almacenadas))
print("La cantidad de veces seguidas que se repitio el color negro fue: {0}".format(veces_almacenadas))
print("La cantidad de veces seguidas que se alterno entre el rojo y el negro: {0}".format(veces_alter_almacenadas))
print("La cantidad de veces seguidas que se nego la segunda docena de la ruleta: {0}".format(docena_almacenada))