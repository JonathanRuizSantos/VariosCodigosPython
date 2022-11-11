# NOTAS:

#1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
#  muy buen ejercicio.

#Ejecucucion -> py 41_Max2Numeros.py

# **************************************************************************************************************** FUNCIONES
from os import system


def Max(num1, num2):
            mayor = 0
            if num1>num2:
                        return num1
            elif num1<num2:
                        return num2
            else:
                        return "Son iguales"
            

# **************************************************************************************************************** PROGRAMA PRINCIPAL
print("")
print("**************************************************************************************************")

print("PROGRAMA QUE PIDE AL USUARIO DOS NUMEROS Y DEVUELVE CUAL ES EL NUMERO MAYOR ENTRE LOS DOS")
print("")

print("Ingresa Dos numeros")
print("--------------------")
numero1 = input("Primer numero: ")
numero2 = input("Segundo Numero: ")

print("")

print('Numero Mayor: {}'.format(Max(numero1,numero2)))

print("")
print("**************************************************************************************************")

system("PAUSE")