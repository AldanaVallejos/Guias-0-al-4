#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 5: Dados dos valores enteros y distintos, emitir
#              una leyenda apropiada que informe cuál es el mayor entre ellos.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: numero1, numero2
# Salidas: mayor
# Procesos: Ingresar numero1
#           Ingresar numero2
#           Determinar cuál es mayor mediante el uso de un if else
#           Mostrar el resultado por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero1=0
numero2=0

# Ingreso de datos
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))

# Determino cuál es el número mayor
if numero1>numero2:
    # Salida por pantalla
    print("El número más grande entre los dos valores ingresados es: {0}".format(numero1))
else:
    # Salida por pantalla
    print("El número más grande entre los dos valores ingresados es: {0}".format(numero2))