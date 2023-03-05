#***********************************************************
# Guia de ejercitación nº2
# Fecha: 15/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 6: Se ingresa un conjunto de valores reales, cada uno de los cuales
#              representan el sueldo de un empleado, excepto el último valor que
#              es cero e indica el fin del conjunto. Se pide desarrollar un programa
#              que determine e informe:
#              a)	Cuántos empleados ganan menos $1.520.
#              b)	Cuántos ganan  $1.520 o más pero menos de $2.780.
#              c)	Cuántos ganan $2.780 o más pero menos de $5.999.
#              d)	Cuántos ganan $5.999 o más.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: sueldo, continuar
# Salidas: sueldoa, sueldob, sueldoc, sueldod
# Procesos: Ingresar sueldos
#           contar los sueldo menores a 1520 -> sueldoa
#           contar los sueldos mayores que 1520 y menores que 2700 -> sueldob
#           Contar los sueldos mayores que 2780 y menores que 5999 -> sueldoc
#           Contar los sueldos mayores que 5999 -> sueldod
#           Parar el programa cuando se ingrese 0
#           Mostrar los resultados por pantalla        
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
sueldo=0.00
continuar="S"
sueldoa=0
sueldob=0
sueldoc=0
sueldod=0

while continuar=="S":
    continuar=="N"
    # Ingreso de dato
    sueldo=float(input("Ingrese el sueldo de un empleado: "))

    if sueldo<1520 and sueldo>=1:
        sueldoa=sueldoa+1
    elif sueldo>=1520 and sueldo<2780:
        sueldob=sueldob+1
    elif sueldo>=2780 and sueldo<5999:
        sueldoc=sueldoc+1
    elif sueldo>=5999:
        sueldod=sueldod+1
    elif sueldo==0:
        break


# Salida por pantalla
print("La cantidad de empleados que ganan menos de $1.520 es: {0}".format(sueldoa))
print("La cantidad de empleados que ganan más de $1.520 pero menos de $2.700 es: {0}".format(sueldob))
print("La cantidad de empleados que ganan más de $2.700 pero menos de $5.999 es: {0}".format(sueldoc))
print("La cantidad de empleados que ganan más de $5.999 es: {0}".format(sueldod))
