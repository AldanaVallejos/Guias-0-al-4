#***********************************************************
# Guia de ejercitación nº2
# Fecha: 15/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 1: Dados 10 valores informar el mayor
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: maximo
# Salidas: mayor
# Procesos: Ingresar 10 valores
#           Informar el mayor por un for in
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
mayor = 0
maximo = 10
 
for i in range(maximo):
    valor = int(input("Ingrese un valor: "))
    if valor > mayor:
        mayor = valor

# Salida por pantalla
print("El mayor es: {0}".format(mayor))
