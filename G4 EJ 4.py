#***********************************************************
# Guia de ejercitación nº2
# Fecha: 16/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: Dado un conjunto de valores, que finaliza con un valor nulo, determinar e imprimir (si hubo valores):
#              a) El valor máximo negativo
#              b) El valor mínimo positivo
#              c) El valor mínimo dentro del rango -17.3 y 26.9
#              d) El promedio de todos los valores.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
null=None
continuar="S"
maximo_n=0
valores=0
minimo=100000000000
cantidad=0
promedio=0.00
contador=0
acumulador=0
minimorango=0

while True:
    try:
        valores=int(input("Ingrese un valor numerico, se cancelara el ingreso con (null): "))
    except ValueError:
        null=True
        break
    
    
    if valores>-17.3 and valores<26.9: #c) El valor mínimo dentro del rango -17.3 y 26.9
        if valores<minimorango:
            minimorango=valores
    
    if valores<0: #Valor maximo negativo
        if valores<maximo_n:
            maximo_n=valores
    
    if valores>0: #valor minimo positivo
        if valores<minimo:
            minimo=valores
    
    acumulador=acumulador+valores 
    contador+=1

    promedio=acumulador/contador #promedio de todos los valores

#Salidas por pantalla
print("El valor máximo negativo es {0}".format(maximo_n))
print("El valor mínimo positivo es {0}".format(minimo))
print("El valor mínimo dentro del rango -17.3 y 26.9 es {0}".format(minimorango))
print("El promedio de todos los valores es {0}".format(promedio))