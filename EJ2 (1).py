#***********************************************************
# Guia de ejercitación nº1
# Fecha: 29/08/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 2: Implementar algoritmos que permitan:
#              a) Calcular el perímetro de un rectángulo dada su base y su altura.
#              b) Calcular el área de un rectángulo dada su base y su altura.
#              c) Calcular el área de un rectángulo (alineado con los
#              ejes x e y) dadas sus coordenadas x1, x2, y1, y2.
#              d) Calcular el perímetro de un círculo dado su radio.
#              e) Calcular el área de un círculo dado su radio.
#              f) Calcular el volumen de una esfera dado su radio.
#              g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#***********************************************************
#                   A N A L I S I S
#***********************************************************
# Entradas: base, altura
#           coorx1 , coorx2 , coory1 , coory2
#           radio , pi
#           cateto1 , cateto2
#           
# Salidas: p_rectangulo
#          a_rectangulo
#          a_rectangulo_coor
#          p_circulo
#          a_circulo
#          volumen
#          hipotenusa
#
# Procesos: 1) Ingresar base 
#           2) Ingresar altura 
#           3) Calcular el perímetro -> p_rectangulo = 2*base+2*altura
#
#           4) Ingresar base
#           5) Ingresar altura
#           6) Calcular el área -> a_rectangulo = base * altura
#
#           7) Ingresar coordenada x1
#           8) Ingresar coordenada x2
#           9) Ingresar coordenada y1
#           10) Ingresar coordenada y2
#           11) Calcular el área de un rectángulo (alineado con los
#           ejes x e y) -> a_rectangulo_coor=[coorx1*coorx2,coory1*coory2]
#
#           12) Ingrese el radio
#           13) Calcular el perímetro del circulo. -> p_circulo = 2*pi*radio
#            
#           14) Ingrese el radio
#           15) Calcular el área de un círculo -> a_circulo = pi*(radio)**2
#
#           16) Ingrese el radio
#           17) Calcular el volumen de una esfera -> volumen = 4/3*pi*(radio)**3
#
#           18) Ingrese el cateto1
#           19) Ingrese el cateto2
#           20) Calcular la hipotenusa -> hipotenusa**2 = cateto1**2 + cateto2**2 
#
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
p_rectangulo=0.00
base=0.00
altura=0.00
a_rectangulo=0.00
a_rectangulo_x1=0.00
a_rectangulo_y1=0.00
a_rectangulo_x2=0.00
a_rectangulo_y2=0.00
coorx1=0.00
coorx2=0.00
coory1=0.00
coory2=0.00
radio=0.00
p_circulo=0.00
a_circulo=0.00
volumen=0.00
cateto1=0.00
cateto2=0.00
hipotenusa=0.00

# Declaración de constantes
pi=3.1416

# A) ALGORITMO QUE CALCULE EL PERÍMETRO DE UN RECTÁNGULO DADA SU BASE Y SU ALTURA

#Ingreso de datos
print("Ingrese el valor de la base")
base=float(input())

print("Ingrese el valor de la altura")
altura=float(input())

#Calculo el perímetro
p_rectangulo=2*base+2*altura

#Salida por pantalla
print("El perimetro del rectángulo con base ",base,"y altura ",altura, " es ", p_rectangulo)

# B) ALGORITMO QUE CALCULE EL ÁREA DE UN RECTÁNGULO DADA SU BASE Y SU ALTURA

#Ingreso de datos
print("Ingrese el valor de la base")
base=float(input())

print("Ingrese el valor de la altura")
altura=float(input())

#Calculo el área
a_rectangulo=base*altura

#Salida por pantalla
print("El área de un rectángulo con base",base,"y altura ",altura," es ", a_rectangulo)

# C) ALGORITMO QUE CALCULE EL ÁREA DE UN RECTANGULO DADAS SUS COORDENADAS

# Ingreso de datos
print("Ingrese el valor de la coordenada x1")
coorx1=float(input())

print("Ingrese el valor de la coordenada y1")
coory1=float(input())

print("Ingrese el valor de la coordenada x2")
coorx2=float(input())

print("Ingrese el valor de la coordenada y2")
coory2=float(input())

#Calculo el área
a_rectangulo_coor=[coorx1*coorx2, coory1*coory2]

#Salida por pantalla
print("El área de el rectángulo dadas sus coordenadas es ", a_rectangulo_coor)

# d) Calcular el perímetro de un círculo dado su radio.

#Ingreso de datos
print("Ingrese el valor del radio")
radio=float(input())

#Calculo el perímetro
p_circulo=2*pi*radio

#Salida por pantalla
print("El perímetro de el circulo es ", p_circulo)

# e) Calcular el área de un círculo dado su radio.

#Ingreso de datos
print("Ingrese el radio del circulo")
base=float(input())

#Calculo el área
a_circulo=pi*(radio)**2

#Salida por pantalla
print("El área del circulo es ", a_circulo)

# f) Calcular el volumen de una esfera dado su radio.

#Ingreso de datos
print("Ingrese el radio de la esfera")
radio=float(input())

#Calculo el volumen
volumen=4/3*pi*(radio)**3

#Salida por pantalla
print("El volumen de la esfera es ", volumen)

# G) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#Ingreso de datos
print("el primer cateto del triángulo rectángulo")
cateto1=float(input())

print("Ingrese el segundo cateto")
cateto2=float(input())

#Calculo la hipotenusa
hipotenusa=cateto1**2 + cateto2**2

#Salida por pantalla
print("El valor de la hipotenusa es ", pow(hipotenusa,2))
