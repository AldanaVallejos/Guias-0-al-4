#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 9: Dado el siguiente enunciado, estrategia y representación
#              gráfica especifique los datos de entrada, de salida y  la
#              codificación en Python. Enunciado: Dados dos números, mostrar 
#              un menú con opciones de sumar, restar o multiplicar dichos 
#              números. Solicite elegir una opción.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: numero1, numero2, eleccion, continuar
# Salidas: suma, resta, multiplicacion
# Procesos: Ingresar numero1
#           Ingresar numero2
#           Muestro un menú
#           Determino la opción elegida
#           Muestro la salida por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero1=0.00
numero2=0.00
suma=0.00
resta=0.00
multiplicacion=0.00
eleccion=""
continuar="S"

#Ingreso de dato
numero1=float(input("Ingrese el número 1: "))
numero2=float(input("Ingrese el número 2: "))

# Creo un ciclo de repetición while
while continuar=="S":
    # Creo un menú de opciones
    print(" SELECCIONE EL OPERADOR QUE DESEE")
    print(" A) Sumar")
    print(" B) Restar")
    print(" C) Multiplicar")
    print(" D) Finalizar y Salir")
    # Ingreso de dato
    eleccion=input()

 #Determino la opción elegida OPCION A) SUMA
    if eleccion=="A":
        # Calculo la suma
        suma=numero1+numero2
        # Salida por pantalla
        print("La suma entre los dos números es: {0}".format(suma))
    
 #Determino la opción elegida OPCION B) RESTA
    if eleccion=="B":
        # Calculo la resta
        resta=numero1-numero2
        # Salida por pantalla
        print("La diferencia entre {0}".format(numero1),"menos {0}".format(numero2),"es igual a: {0}".format(resta))

 #Determino la opción elegida OPCION C) MULTIPLICACION
    if eleccion=="C":
        # Calculo la multiplicación
        multiplicacion=numero1*numero2
        # Salida por pantalla
        print("La multiplicación entre los dos números da como resultado: {0}".format(multiplicacion))

 # Opcioón D) SALIR Y FINALIZAR
    if eleccion=="D":
        continuar="N"
