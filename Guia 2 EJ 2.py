#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 2: Dado el siguiente enunciado y su representación gráfica 
#              especifique los datos de entrada, de salida, estrategia, 
#              seguimiento y codificación. Enunciado: Dado un número real
#              que representa el importe de una compra informar las 
#              posibles formas de pago, según la siguiente tabla:
#              1 cuota  de $................. 
#              2 cuotas de $................. total $................. (   5% de recargo)
#              6 cuotas de $................. total $................. ( 40% de recargo)
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: importe
# Salidas: cuota2, cuota6
# Procesos: Ingresar importe de la compra
#           Calcular las 2 cuotas y 6 cuotas + los recargos
#           Muestro un menú de opciones en pantalla
#           Determinar la opción elegida y terminar el proceso
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
importe=0.00
cuota2=0.00
cuota6=0.00
total2c=0.00
total6c=0.00
eleccion=0

#Ingreso de dato
importe=float(input("Ingrese el importe de la compra: "))

# Calculo las 2 cuotas con recargo de 5%
cuota2=importe/2
total2c=importe+(5/100*importe)

# Calculo las 6 cuotas con recargo de 40%
cuota6=importe/6
total6c=importe+(40/100*importe)

#Realizo un menú de opciones
print("Seleccione la forma de pago que desee")
print(" 1 cuota de ${0}".format(importe),"--------------------------------------> INGRESE UNA A")
print(" 2 cuotas de ${0}".format(cuota2),"total ${0}".format(total2c)," (5% de recargo) ------> INGRESE UNA B")
print(" 6 cuotas de ${0}".format(cuota6),"total ${0}".format(total6c)," (40% de recargo) ------> INGRESE UNA C")
