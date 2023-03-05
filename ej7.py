#***********************************************************
# Guia de ejercitación nº0
# Fecha: 26/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 7: Escribir un programa que pida al usuario dos
#              números enteros y muestre por pantalla
#              “la division <n> entre <m> da un cociente <c>
#              y un resto <r>” donde <n> y <m> son los números
#              introducidos por el usuario, y <c> y <r> son el
#              cociente y el resto de la división entera
#              respectivamente.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: nro1, nro2
# Salidas: cociente, resto
# Procesos: Ingreso nro1
#           Ingreso nro2
#           Calculo el cociente -> cociente=nro1/nro2
#           Calculo el resto -> resto=nro1%nro2
#           Muestro por pantalla el cociente y resto
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nro1=0
nro2=0
cociente=0
resto=0

# Ingreso de datos
print("Ingrese un numero entero")
nro1=int(input())
print("Ingrese otro numero entero")
nro2=int(input())

#Calculo el cociente
cociente=(nro1/nro2)
#Calculo el resto
resto=(nro1%nro2)

#Salida por pantalla
print("La división",nro1,"entre",nro2,"da un cociente:",cociente,"y un resto:",resto)
