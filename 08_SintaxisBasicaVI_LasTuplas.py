mitupla=("juan",13,1,1995) #declaracion de una tupla
milista=list(mitupla) #transforma una tupla en una lista llamada milista
print(mitupla[2])  #imprime el elemento 2 de la tupla que en este caso es 1
print(milista)    #imprime la lista llamada milista
print(mitupla)    #imprime la tupla llamada mitupla

milista=["juan", 13,1,1995] #esta es una lista llamada mi lista
mitupla=tuple(milista)  #transforma una lista en tupla que llamaremos mitupla
print(mitupla)    #imprime una tupla llamada mitupla

print("juan" in mitupla) #esta instruccion me dice si "juan" se encuentra dentro de la tupla mitupla, si es verdad se imprime true, si no se imprime false
print("juan222" in mitupla) # me devuelve falso porque no se encuentra ese nombre en la lista
print(mitupla.count(13))  #me devuelve la cantidad de veces que se encuentra un elemento en una tupla
print(len(mitupla)) # me dice cuantos elementos hay en una tupla

mitupla=("juan",) #a esto se le llama tupla unitaria
print(len(mitupla)) # se imprime la tupla unitaria

mitupla="juan",13,1,1995    #esto tambien es una tupla, se puede poner pero no es recomedable, a esto se llama empaquetado de tupla
print(mitupla)  #imprime la tupla anterior

mitupla=("juan",13,1,1995)    #a esto se le conoce como desempaquetado, todo este bloque de codigos
nombre,dia,mes,agno=mitupla
print(nombre)
print(dia)
print(agno)
print(mes)