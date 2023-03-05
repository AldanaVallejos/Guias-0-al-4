#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 1: A partir de dos valores enteros A y B, informar
#              la suma, la diferencia (A menos B), y el producto.
#              Estrategia:
#	           Solicitar e ingresar datos por teclado
#	           Calcular suma e informar por monitor
#	           Calcular diferencia e informar por monitor
#	           Calcular producto e informar por monitor
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: A, B
# Salidas: suma, resta, producto
# Procesos: Ingresar numero A
#           Ingresar numero B
#           Calcular la suma y mostrar en pantalla
#           Calcular la resta y mostrar en pantalla
#           Calcular el producto y mostrar por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
A=0
B=0
suma=0
resta=0
producto=0

# Ingreso de datos
A=int(input("Ingrese el primer número entero: "))
B=int(input("Ingrese el segundo número entero: "))

# Calculo la suma entre los dos valores
suma=A+B

# Muestro el resultado en pantalla
print("El resultado de la suma es: {0}".format(suma))

# Calculo la diferencia entre los dos valores
resta=A-B

# Muestro el resultado en pantalla
print("El resultado de la resta es: {0}".format(resta))

# Calculo el producto entre los dos valores
producto=A*B

# Muestro el resultado en pantalla
print("El resultado del producto es: {0}".format(producto))