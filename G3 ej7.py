#***********************************************************
# Guia de ejercitación nº3
# Fecha: 23/09/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 7: Dado un valor M determinar y emitir un listado con
#              los M primeros múltiplos de 3 que no lo sean de 5,
#              dentro del conjunto de los números naturales.
#***********************************************************
# Declaración de variables
M=0
contador=0
numero=0


# Ingreso de dato
try: #validación
    M=int(input("Ingrese el valor: "))
except ValueError:
    print("Error. Ingrese un número")
    M=int(input("Ingrese el valor: "))

print("Los primeros {0} multiplos de 3 que no son multiplos de 5 son: ".format(M)) #Salida por pantalla
while contador<M:
        if numero%3==0 and numero%5!=0:
            multiplo=numero
            # Incremento el contador
            contador+=1
            print(numero) #Listado de los multiplos
        
        numero+=1

