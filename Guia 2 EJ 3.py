#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 3: Dada una terna de números naturales que representan al día,
#              al mes y al año de una determinada fecha informarla 
#              como un solo número natural de 8 dígitos (AAAAMMDD).
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: año, dia, mes
# Salidas: añomesdia
# Procesos: Ingresar el año
#           Ingresar el mes
#           Ingresar el dia
#           Unir los valores con str
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
año=0
dia=0
mes=0

# Ingreso de datos
año=int(input("Ingrese el año: "))
mes=int(input("Ingrese el mes: "))
dia=int(input("Ingrese el dia: "))

# Salida por pantalla
print("Usted ingresó el "+str(año)+str(mes)+str(dia))