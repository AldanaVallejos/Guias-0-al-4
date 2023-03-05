#***********************************************************
# Guia de ejercitación nº1
# Fecha: 30/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 9:  Escribir un programa que utilice la función
#               anterior para generar una tabla de conversión
#               de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10. 
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: 
# Salidas: 
# Procesos: Definir una función que termine en la ecuación prevista
#           Muestro por pantalla las tablas
#***********************************************************
#                    D I S E Ñ O
#***********************************************************

# Defino la función
def ecuacion(c):
    return 9/5 * c + 32
#Salida por pantalla
print ("Grados Fahrenheit // Grados Celsius")
for grados in range(0,121,10):
    print ("       ",grados,"        ",ecuacion(grados))

