#PROGRAMA DE CALCULADORA DE SUMA,RESTA, MULTIPLICACION, DIVISION CON FUNCIONES

from distutils.command.clean import clean
from re import X
from tkinter import Button, Variable
from turtle import clear


clean
clear
from ast import If
from cmath import sin, sinh, tan
from math import cos


def menu():
            print("Calculadora Basica 01")
            print("    ")
            print("Menu")
            print("01. Suma")
            print("02. Resta")
            print("03. Multiplicacion")
            print("04. Division")
            print("05. Potencia")
            print("06. Sen")
            print("07. Cos")
            print("08. Tan")
            print("09. Senh")
            global opcion
            opcion=int(input("Selecciona una opcion: "))


def op():
            global x1,x2
            x1=int(input("Ingresa X1: "))
            x2=int(input("Ingresa X2: "))


def Suma():
            global r
            r=x1+x2
            return r

def Resta():
            global r
            r=x1+x2
            return r

def Multiplica():
            global r
            r=x1*x2
            return r

def Divide():
            global r
            r=x1/x2
            return r

def Potencia():
            global r
            r=pow(x1,x2)
            return r

def Sen():
            global r
            r=sin(x1)
            return r

def Cos():
            global r
            r=cos(x1)
            return r

def Tan():
            global r
            r=tan(x1)
            return r

def Senh():
            global r
            r=sinh(x1)
            return r

def MenuRev():
            global M
            print("S. Salir")
            print("C. Continuar")
            M=input("Selecciona S/C : ")

#Inicia programa

while True:
            print("*************************************************************************")
            print("*************************************************************************")
            print("")

            menu()
            op()
            print("    ")
            if opcion==1:
                        Suma()
                        print(x1," + ",x2," = ",r)
            elif opcion==2:
                        Resta()
                        print(x1," - ",x2," = ",r)
            elif opcion==3:
                        Multiplica()
                        print(x1," * ",x2," = ",r)
            elif opcion==4:
                        Divide()
                        print(x1," / ",x2," = ",r)
            elif opcion==5:
                        Potencia()
                        print(x1," ^ ",x2," = ",r)
            elif opcion==6:
                        Sen()
                        print(" Sin (",x1,") = ",r)
            elif opcion==7:
                        Cos()
                        print(" Cos (",x1,") = ",r)
            elif opcion==8:
                        Tan()
                        print(" Tan (",x1,") = ",r)
            elif opcion==9:
                        Senh()
                        print(" Sinh (",x1,") = ",r)
            else:
                        print("Error, opcion no valida")

            MenuRev()

            if(M=="S"):
                        break


            