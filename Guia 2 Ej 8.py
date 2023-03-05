#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 8: Dados un mes y el año correspondiente informar cuantos días tiene el mes.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: mes, año
# Salidas: 30 dias, 31 dias, 28 dias
# Procesos: Ingresar mes
#           Ingresar año
#           Determinar cuantos dias tiene el mes
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
mes=0
año=0

# Ingreso de datos
año=int(input("Ingrese el año: "))
mes=int(input("Ingrese el mes: "))

if mes==9 or mes==4 or mes==6 or mes==11:
    print("El mes tiene 30 días")
else:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print("El mes tiene 31 días")
    else:
         print("El mes tiene 28 días")