#Este programa calcula el puntaje final de respuestas correctas, incorrectas y en blanco
#Correctas 3Puntos
print("     ")
Correctas=int(input("respuestas correctas: "))
Incorrectas=int(input("respuestas incorrectas: "))
Blanco=int(input("respuestas en blanco: "))

TotalPreguntas=Correctas+Incorrectas+Blanco

PuntosIncorrectas=Incorrectas*3
PuntosBlanco=Blanco*3
PuntosTotal=(TotalPreguntas*3)-PuntosIncorrectas-PuntosBlanco
print("Total de puntaje: ",PuntosTotal)

