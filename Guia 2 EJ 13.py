#***********************************************************
# Guia de ejercitación nº2
# Fecha: 08/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 13: Escribir un algoritmo que permita encontrar:
#               a) El máximo o mínimo de un polinomio de segundo grado
#               (dados los coeficientes a, b y c), indicando si es un máximo o un mínimo. 
#               b) Las raíces (reales) de un polinomio de segundo grado. Nota: validar
#               que las operaciones puedan efectuarse antes de realizarlas (no dividir
#               por cero, ni calcular la raíz de un número negativo). 
#               c) La intersección de dos rectas (dadas las pendientes y ordenada
#               al origen de cada recta). Nota: validar que no sean dos rectas con
#               la misma pendiente, antes de efectuar la operación.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: a, b, c, x, y
# Salidas: v
# Procesos: a) Ingresar los coeficientes a, b y c
#              Calcular el valor de x -> x=-(b)/(2*a)
#              Calcular el valor de y -> y=(c)-((b)*2)/(4*(a))
#              Calcular el vértice -> v=[x, y]
#              Mostrar tiene un minimo (si a es positiva) en v=[x, y]
#              Mostrar tiene un máximo (si a es negativa) en v=[x, y]
#
#           b) Ingresar los coeficientes a, b y c
#              Calcular r1=b*2-4*a*c
#              Verificar que no de 0 ni -
#              Calcular x=(-b+pow(r1))/  2*a -> verificar que no de 0
#              Calcular y=(-b-pow(r1))/  2*a
#              raices=[x, y]
#              Mostrar ("Las raices del polinomio son", (raices))
#
#           c) Ingresar los coeficientes a, b y c
#              Ingresar los coeficientes d, e y f
#              Calculo el determinante -> determinante=a*e - b*d
#              Calculo los sistemas de ecuacion -> x=(c*e - b*f) / determinante
#                                                  y= (a*f - c*d) / determinante
#              Mostrar la intersección por pantalla
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
#              Calcular [x, y]=(-b+-pow((b)*2-4*a*c))/2*a
a=0
b=0
c=0
v=0
x1=0
x2=0
r1=0
d=0
e=0
f=0
determinante=0

#a)
# Ingreso de datos
a=int(input("Ingrese el primer coeficiente (a): "))
b=int(input("Ingrese el segundo coeficiente (b): "))
c=int(input("Ingrese el tercer coeficiente (c): "))

# Calculo el valor de x
x=-(b)/(2*a)

# Calculo el valor de y
y=(c)-((b)*2)/(4*(a))

# Vértice
v=[x, y]

# Determino si es un punto maximo o minimo
if a<0:
    print("Tiene un máximo en", v)
else:
    if a>0:
        print("Tiene un minimo en", v)

#b)
# Ingreso de datos
a=int(input("Ingrese el primer coeficiente (a): "))
b=int(input("Ingrese el segundo coeficiente (b): "))
c=int(input("Ingrese el tercer coeficiente (c): "))

# Realizo formula de bhaskara
r1=(b)*2-(4*(a)*(c))

# Verifico que no de 0 ni -
if r1==0 or r1<0:
    print("ERROR - INGRESE OTROS NUMEROS")

# Calculo x=(-b+pow(r1))/  2*a -> verificar que no de 0
import math
x1=(-b)+math.sqrt((r1)/ 2*(a))

if a==0:
    print("ERROR - INGRESE OTROS NUMEROS")

# Calculo y=(-b-pow(r1))/  2*a
import math
x2=(-b)-math.sqrt((r1)/ 2*(a))

print("Las raices del polinomio son", (x1,x2))

#c)
# Ingreso de datos
a=int(input("Ingrese el primer coeficiente (a): "))
b=int(input("Ingrese el segundo coeficiente (b): "))
c=int(input("Ingrese el tercer coeficiente (c): "))
d=int(input("Ingrese el coeficiente (d): "))
e=int(input("Ingrese el coeficiente (e): "))
f=int(input("Ingrese el coeficiente (f): "))

def interseccion(a, b, c, d, e, f):
    # Calculo el determinante
    determinante=a*e - b*d

    if determinante!=0:
        # Calculo los sistemas de ecuacion
        x=(c*e - b*f) / determinante
        y= (a*f - c*d) / determinante
        return x,y
    else:
        # Salida por pantalla
        return "ERROR INGRESE OTROS NÚMEROS"

# Salida por pantalla
print(interseccion(a, b, c, d, e, f))