#***********************************************************
# Guia de ejercitación nº2
# Fecha: 04/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 6: Dadas dos fechas informar cual es la más reciente.
#              Determine cuales serían los datos de entrada  y las 
#              leyendas a informar de acuerdo al proceso solicitado.    
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: fecha1, fecha2, fechaactual, diferencia, diferencia2, continuar
# Salidas: la mas reciente
# Procesos: Ingresar fechaactual
#           Ingresar fecha1
#           Ingresar fecha2
#           Validar que sean fechas pasadas
#           Validar que no sean fechas iguales
#           Calculo las diferencias -> diferencia=fechaactual-fecha1
#                                      diferencia2=fechaactual-fecha2
#           Muestro el resultado en pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
fechaactual=0
fecha1=0
fecha2=0
continuar="S"
diferencia=0
diferencia2=0

while continuar=="S":
    # Ingreso de datos
    fechaactual=int(input("Ingrese la fecha actual en orden (AAAAMMDD): "))
    fecha1=int(input("Ingrese la primera fecha en orden (AAAAMMDD): "))
    fecha2=int(input("Ingrese la segunda fecha en orden (AAAAMMDD): "))
    
    # Verifico que no sean fechas futuras a la actual
    if fecha1>fechaactual or fecha2>fechaactual:
        # Salida por pantalla
         print("Error - Ingrese una fecha pasada a la actual")
         
    # Verifico que no sean fechas iguales
    if fecha1==fecha2:
        # Salida por pantalla
        print("Error - Ingrese fechas distintas")
    continuar="N"

# Calculo la diferencia entre la fecha actual menos las fechas
diferencia=fechaactual-fecha1
diferencia2=fechaactual-fecha2

if diferencia<diferencia2:
    # Salida por pantalla
    print("La primera fecha es la más reciente")
else:
    # Salida por pantalla
    print("La segunda fecha es la más reciente")

