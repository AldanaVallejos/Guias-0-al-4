#***********************************************************
# Guia de ejercitación nº0
# Fecha: 26/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 6: Escribir un programa que pida al usuario su peso
#             (en kg) y estatura (en metros), calcule el índice
#              de masa corporal y lo almacene en una variable,
#              y muestre por pantalla la frase “Tu indice de masa
#              corportal es <imc>” donde <imc> es el indice de
#              masa corporal calculado redondeado con dos decimales.      
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: peso, estatura
# Salidas: imc
# Procesos: Ingresar peso
#           Ingresar estatura
#           Calcular indice de masa corporal -> imc= peso/(estatura)**2
#           Redondear con dos decimales -> round(imc,2)
#           Mostrar imc
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
peso=0.00
estatura=0.00
imc=0.00

#Ingreso de datos
print("Ingrese su peso en kg")
peso=int(input())
print("Ingrese su estatura en m")
estatura=float(input())

#Calculo indice de masa corporal
imc=(peso)/(estatura**2)

#Salida por pantalla
print("Tu indice de masa corporal es {0}".format(round(imc,2)))
