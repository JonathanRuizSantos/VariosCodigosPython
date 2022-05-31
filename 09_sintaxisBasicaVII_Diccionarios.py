midiccionario={"Alemania":"Berlin","Francia":"Parìs","Reino Unido":"Londres","España":"Madrid"} #esta es la sintaxis del diccionario llamado midiccionario
print(midiccionario["Francia"])  #imprime la clave del elemento francia que es paris
print(midiccionario) #imprime todo el diccionario

midiccionario["Italia"]="Lisboa" #se agrega un nuevo elemento a midiccionario pero hay un error a proposito
print(midiccionario)    #se imprime el diccionario con el elemento agregado

midiccionario["Italia"]="Roma"      #se corrige el error anterior, ahora roma es la capital del italia
print(midiccionario)    #muestra que ya se corrigio el error

del midiccionario["Reino Unido"]    #elimina  a reino unido de midiccionario
print(midiccionario)

midiccionario={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3} #el diccionario puede contener no solo valores de tipo string sino tambien numericos
print(midiccionario) 

mitupla=["España","Francia","Reino Unido","Alemania"] #se crea una tupla para despues transformarse a un diccionario
midiccionario={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}  #se utiliza la tupla anterior para agregarse al diccionario
print(midiccionario) # se imprime el diccionario llamado midiccionario
print(midiccionario["Francia"]) #imprime el valor asignado en uno de la tupla o se puede poner midiccionario["Francia"] es lo mismo

midiccionario={23:"Jordan", "Nombre": "MIchael", "Equipo":"Chicago" , "Anillos":[1991,1992,1993,1997,1998]} #se crea un diccionario
print(midiccionario) #se imprime el diccionario completo
print(midiccionario["Equipo"])
print(midiccionario["Anillos"])

midiccionario={23:"Jordan","Nombre":"MIchael","Equipo":"Chicago" ,"Anillos":{"temporadas":[1991,1992,1993,1997,1998]}}  #esto es un diccionario dentro de otro diccionario
print(midiccionario["Anillos"])
print(midiccionario)

print(midiccionario.keys())  #claves de midiccionario
print(midiccionario.values()) #valores de midiccionario
print(len(midiccionario))     #longitud de midiccionario
