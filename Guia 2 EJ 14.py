#***********************************************************
# Guia de ejercitación nº2
# Fecha: 08/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 14: Suponiendo que el primer día del año fue lunes,
#               escribir un programa que reciba un número con el
#               día del año (de 1 a 366) y devuelva el día de la
#               semana que le toca. Por ejemplo: si recibe '3' debe
#               devolver 'miércoles', si recibe '9' debe devolver 'martes'. 
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: dia, resto, entero
# Salidas: lunes, martes, miércoles, jueves, viernes, sabado, domingo
# Procesos: Ingreso el dia
#           Planteo una division para sacar el resto -> dia%7
#           Si resto=0 print "domingo"
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
dia=0
resto=0
entero=0

# Ingreso de dato
dia=int(input("Ingrese el número del día: "))
#Calculo el resto de la division por 7
resto=dia%7

if resto==1:
    # Salida por pantalla
    print("Lunes")
else:
    if resto==2:
        # Salida por pantalla
        print("Martes")
    else:
        if resto==3:
            # Salida por pantalla
            print("Miércoles")
        else:
           if resto==4:
               # Salida por pantalla
               print("Jueves")
           else:
                if resto==5:
                    # Salida por pantalla
                    print("Viernes")
                else:
                    if resto==6:
                        # Salida por pantalla
                        print("Sábado")
                    else:
                        if resto==7:
                            # Salida por pantalla
                            print("Domingo")


if resto==0:
    entero=dia//7

    if 1<=entero<=52:
        # Salida por pantalla
        print("Domingo")