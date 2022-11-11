#Programa que calcula el numero de partidos ganados, empatados y perdidos

PG=int(input("Partidos ganados = "))
PE=int(input("Partidos empatados = "))
PP=int(input("Partidos perdidos = "))

puntosPG=PG*3
puntosPE=PE*1
puntosPP=PE*0

TotalPuntos=puntosPG+puntosPE+puntosPP

print("Total de puntos : ",TotalPuntos)