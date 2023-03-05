#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 10: Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas:
#	            ‘menor’ si la edad es menor o igual a 12  
#	            ‘cadete’ si la edad está comprendida entre 13 y 18
#	            ‘juvenil’ si la edad es mayor que 18 y no supera los 26
#	            ‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: edad
# Salidas: menor, mayor, cadete, juvenil
# Procesos: Ingresar una edad
#           Determinar cuál leyenda es -> utilización del if
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
edad=0

# Ingreso de dato
edad=int(input("Ingrese la edad: "))

# Creo un condicional
if edad<=12:
    print("Es menor")
else:
    if 13<edad<18:
        print("Es cadete")
    else:
        if 18<edad<26:
            print("Es juvenil")
        else:
            print("Es mayor")