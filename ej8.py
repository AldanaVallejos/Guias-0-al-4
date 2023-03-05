#***********************************************************
# Guia de ejercitación nº0
# Fecha: 26/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 8: Imagina que acabas de abrir una nueva cuenta
#              de ahorros que te ofrece el 4% de interés al
#              año. Estos ahorros debido a intereses, que
#              no se cobran hasta finales de año, se te añaden
#              al balance final de tu cuenta de ahorros.
#              Escribir un programa que comience leyendo la
#              cantidad de dinero depositada en la cuenta de
#              ahorros, introducida por el usuario. Después
#              el programa debe calcular y mostrar por pantalla
#              la cantidad de ahorros tras el primer, segundo
#              y tercer años. Redondear cada cantidad a dos decimales.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: ahorro_inicial, interes
#
# Salidas: primer_ahorro, segundo_ahorro, tercer_ahorro
#
# Procesos: Ingresar el monto que deposito en la cuenta de ahorros 
#           Calcular la cantidad de ahorros tras el primer año -> primer_ahorro=(ahorro_inicial*interes/100)+ahorro_inicial
#           Calcular la cantidad de ahorros tras el segundo año -> segundo_ahorro=(primer_ahorro*interes/100)+primer_ahorro
#           Calcular la cantidad de ahorros tras el tercer año -> tercer_ahorro=(segundo_ahorro*interes/100)+segundo_ahorro
#           Mostrar por pantalla los calculos redondeados a dos decimales
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
ahorro_inicial=0.00
primer_ahorro=0.00
segundo_ahorro=0.00
tercer_ahorro=0.00

# Declaración constantes
interes=4

# Ingreso de datos
print("Ingrese la cantidad de dinero depositado en la cuenta de ahorros")
ahorro_inicial=float(input())

# Calculo cantidad de ahorros tras el primer año
primer_ahorro=(ahorro_inicial*interes/100)+ahorro_inicial
# Calculo cantidad de ahorros tras el segundo año
segundo_ahorro=(primer_ahorro*interes/100)+primer_ahorro
# Calculo cantidad de ahorros tras el tercer año
tercer_ahorro=(segundo_ahorro*interes/100)+segundo_ahorro

# Salida por pantalla
print("La cantidad de ahorros tras el primer año fue de: {0}".format(round(primer_ahorro,2)))
print("La cantidad de ahorros tras el segundo año fue de: {0}".format(round(segundo_ahorro,2)))
print("La cantidad de ahorros tras el tercer año fue de: {0}".format(round(tercer_ahorro,2)))
