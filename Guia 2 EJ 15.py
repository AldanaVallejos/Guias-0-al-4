#***********************************************************
# Guia de ejercitación nº2
# Fecha: 08/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 15: Escribir un programa que reciba como entrada un entero
#               representando un año (por ejemplo 751, 1999, o 2158), y
#               muestre por pantalla el mismo año escrito en números romanos.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: año
# Salidas: enterosaromanos
# Procesos: Ingreso el año
#           Creo una función de conversión mediante listas
#           Muestro el resultado en pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
año=0

# Ingreso de dato
año=int(input("Ingrese el año: "))

# Creo una función
def enterosaromanos(entero):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]

        i += 1
    
    return numeral

# Salida por pantalla
print(enterosaromanos(año))
