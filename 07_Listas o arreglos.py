#aqui se mostrara la sintaxis de las listas o arreglos en python

#Ejemplo 1
alumnos=["juan","pepe","calitos","nicolas","federico","nora"]  #arreglo de 6 elementos de indice 0 a indice 5
print(alumnos[:]) #imprime la lista de alumnos completa
print(alumnos[0:3]) #imprime la lista de alumnos del indice 0 al indice 3
print(alumnos[5]) #imprime el nombre del alumno de la posicion 5; nora
print(alumnos[-3])#imprime el nombre del alumno de la posicion 3 de derecha a izquierda;nicolas
#print(alumnos[8])#genera un error porque no existe ese dato
alumnos.append("Jhovani")#Agrega a Jhovania al final de la lista alumnos
print(alumnos[:])
alumnos.insert(3,"Zaira")#Agrega a zaira en la posicion 3, es decir, entre carlitos y nicolas
print(alumnos[:])
alumnos.extend(["mario","marcos","luis","rodrigo","laura","Jimena"])#agrega al final de la lista alumnos esta nueva lista
                                                                  #dando como resultado una lista alumnos extendida hacia la derecha

print(alumnos[:])
print(alumnos.index("mario"))#me indica en que posicion de la lista se encuentra mario, es la posicion 8
alumnos.remove("calitos")#esta funcion removera a carlitos de la lista
print(alumnos[:])
alumnos.pop()           #elimina el ultimo elemento de la lista; jimena
print(alumnos[:])

#ahora sumaremos dos listas diferentes
alumnos2=["mia","mariana","marisol","ramon"]
alumnos3=alumnos+alumnos2           #de esta manera se suman dos listas diferentes
print(alumnos3[:])

#ahora multiplicaremos una lista
alumnos3=alumnos+alumnos2           #asi se repetiran los datos de lista3 3 veces
alumnos4=alumnos3*3
print(alumnos4[:])