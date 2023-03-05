#***********************************************************
# Guia de ejercitación nº1
# Fecha: 29/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 5: Implementar algoritmos que resuelvan los siguientes problemas:
#              a) Dados dos números, imprimir la suma, resta, división y
#              multiplicación de ambos. 
#              b) Dado un número entero n, imprimir su tabla de multiplicar.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: a) numero1 , numero2
#           b) n
#
# Salidas: a) suma, resta, división, multiplicación
#          b) tabla
#
# Procesos: 1) Ingresar numero1
#           2) Ingresar numero2
#           3) Calcular la suma, resta, división y multiplicación
#           4) Mostrar por pantalla
#           5) Ingresar un número entero
#           6) Mostrar su tabla de multiplicar
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero1=0.00
numero2=0.00
n=0

#Declaración de constantes
desde=1
hasta=10

#Ingreso de datos
print("Ingrese el primer número")
numero1=float(input())

print("Ingrese el segundo número")
numero2=float(input())

#Salida por pantalla
print("La suma entre",numero1, "y",numero2, "es", (numero1+numero2), "la resta es",(numero1-numero2), "la división es", (numero1/numero2), "y la multiplicación es", (numero1*numero2))

#Ingreso de dato
print("Ingrese un nímero entero")
n=int(input())

#Calculo la tabla de multiplicar
for f in range(desde, hasta + 1):
	print(f'{n} x {f} =  {n * f}')
	