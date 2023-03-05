#***********************************************************
# Guia de ejercitación nº4
# Fecha: 24/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 5: Se dispone de un lote de valores enteros positivos que finaliza
#              con un número negativo. El lote está dividido en sublotes por
#              medio de valores cero. Desarrollar un programa que determine e informe:
#              a)	por cada sublote el promedio de valores -> ()+()+()/3 LISTO
#              b)	el total de sublotes procesados LISTO
#              c)	el valor máximo del conjunto, indicando en que sublote se encontró y la posición relativa del mismo dentro del sublote LISTO
#              d)	valor mínimo de cada sublote
#              Nota: el lote puede estar vacío (primer valor negativo), o puede haber uno, varios o todos los sublotes vacíos (ceros consecutivos)
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
lotevalores=0
continuar="S"
totalsublotes=0
divisor=0
acumulador=0
promedio=0.00
maximoconjunto=0
pos_max_sublote=0
posicion=0
sublote=0
minimo=100000000
numeros=[]
minimosublote=0

while continuar=="S":
    try: #Validacion
        lotevalores=int(input("Ingrese los valores del lote (finaliza con un numero negativo): ")) #Ingreso de dato
    except ValueError:
        print("Error. Tiene que ingresar un numero")
        lotevalores=int(input("Ingrese los valores del lote (finaliza con un numero negativo): "))

    if lotevalores<0:
        continuar="N"
    else:
        numeros.append(lotevalores)
        if lotevalores!=0 and lotevalores>0:
            divisor+=1

    if lotevalores==0: # b)total de sublotes procesados
        totalsublotes+=1

    if lotevalores<minimo and lotevalores!=0 and lotevalores>0:
        minimo=lotevalores
    
    if lotevalores>0:
        acumulador=acumulador+lotevalores

    promedio=acumulador/divisor # a)promedio de valores

    for i in numeros:
        if i>maximoconjunto: # c.1) Valor máximo del conjunto
            maximoconjunto=i
            sublote=totalsublotes+1 # c.2) en que sublote se encontró
            posicion=numeros.index(i)
    
    if totalsublotes>0: #minimo del sublote
        if totalsublotes==0:
            if lotevalores<minimo:
                minimo=lotevalores

#Salidas por pantalla
print("El promedio de los valores ingresados es {0}".format(promedio))
print("El total de sublotes procesados es {0}".format(totalsublotes))
print("El valor máximo del conjunto es %d, se encontró en el sublote %d, y su posicion dentro del sublote es %d" %(maximoconjunto, sublote, posicion+1))
print("El valor minimo del sublote es {0}".format(minimo))
