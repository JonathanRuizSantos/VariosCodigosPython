'''
PROGRAMA QUE SIMULA EL USO DE LOS DADOS. SE PRESENTA LA OPCION DE USAR UN SOLO DADO, DOS , O HASTA TRES DADOS
GENERANDO NUMEROS ALEATORIAMENTE ENTRE 1 Y 6 EN CADA DADO.

FECHA DE INICIO DE CODIFICACION: 01/11/2022
FECHA DE ULTIMA ACTUALIZACION DE CODIGO 04/11/2022
VERSION 22.1

COMPUTECH, JONATHAN RS
scompu90@gmail.com
'''

import random
from os import system

# **************************************************************************** FUNCIONES
def dadoAleatorio():
            aleatorio = random.randint(1,6)
            return aleatorio

def menuSaldia():
            opRepite = 0
            while(opRepite < 1 or opRepite > 2):
                        opRepite = int(input("Presiona 1 para un nuevo aleatorio o 2 para salir al menu\n"))

            if opRepite == 1:
                        llaveciclo = True
                        llave = True                        
            elif opRepite == 2:
                        llaveciclo = False
                        llave = True
            

            return llave, llaveciclo
# ***************************************************************************** PROGRAMA PRINCIPAL

llave = True
while(llave == True):
            contador = 0
            llaveciclo = True

            print("\n\n*********************************************************************************\n")
            print("PROGRAMA QUE SIMULA EL USO DE LOS DADOS CON DIFERENTES OPCIONES Y DE FORMA ALEATORIA")

            print("\n**********************************************************************************")
            print("********* Menu *********")
            print("(1) Tiro con un dado")
            print("(2) Tiro con dos dados")
            print("(3) Tiro con tres dados")
            print("(4) Salir\n")

            opcion = int(input("Yo Elijo: "))
            system("cls")

            if opcion == 1:
                        while llaveciclo == True:
                                    print("************ TIRO CON UN DADO ***************")
                                    contador = contador + 1
                                    dado1 = dadoAleatorio()
                                    print("Tiro {}: {}".format(contador,dado1))
                                    print("\n*********************************************")
                                    llave, llaveciclo = menuSaldia()
                                    system("cls")

                        llave == False
                                    

            elif opcion == 2:
                        while llaveciclo == True:
                                    print("************ TIRO CON DOS DADO ***************")
                                    contador = contador + 1
                                    dado1 = dadoAleatorio()
                                    dado2 = dadoAleatorio()
                                    print("Tiro {}: {}".format(contador,dado1))
                                    print("Tiro {}: {}".format(contador,dado2))
                                    suma = dado1 + dado2
                                    print("Suma: {}".format(suma))
                                    print("\n*********************************************")
                                    llave, llaveciclo = menuSaldia()
                                    system("cls")

                        llave == False
            elif opcion == 3:
                        while llaveciclo == True:
                                    print("************ TIRO CON TRES DADO ***************")
                                    contador = contador + 1
                                    dado1 = dadoAleatorio()
                                    dado2 = dadoAleatorio()
                                    dado3 = dadoAleatorio()
                                    print("Tiro {}: {}".format(contador,dado1))
                                    print("Tiro {}: {}".format(contador,dado2))
                                    print("Tiro {}: {}".format(contador,dado3))
                                    suma = dado1 + dado2 + dado3
                                    print("Suma: {}".format(suma))
                                    print("\n*********************************************")
                                    llave, llaveciclo = menuSaldia()
                                    system("cls")

                        llave == False
            elif opcion == 4:
                        llave = False
                        exit()
            else:
                        print("------------------------")
                        print("\nESA OPCION NO EXISTE")
                        print("------------------------")
                        system("pause")
                        system("cls")
                        llave = True

system("pause")
