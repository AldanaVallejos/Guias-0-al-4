#***********************************************************
# Guia de ejercitación nº2
# Fecha: 15/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 5: Ingresar e informar valores, mientras que el valor 
#              ingresado no sea negativo. Informar la cantidad de valores ingresados.   
#
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: valor, continuar
# Salidas: cantidad
# Procesos: Pedir al usuario ingresar numeros
#           Contar los numeros positivos
#           Mostrar los positivos por pantalla     
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
valor=0.00
cantidad=0
continuar="S"

while continuar=="S":
    continuar="N"
    # Ingreso de dato
    valor=float(input("Ingrese un número: "))
    
    #Utilizo un contador para contar solo los números positivos
    if valor>0:
        cantidad=cantidad+1
    
    # Ingreso de dato
    print("Desea ingresar otro número? S/N")
    continuar=input()

# Salida por pantalla
print("Usted ingresó {0}".format(cantidad),"valores positivos")
