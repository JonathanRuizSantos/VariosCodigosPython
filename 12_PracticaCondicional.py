#.................Ejemplo 1
edad=700

if 0<edad<100:  #concatenacion con operadores de comparacion
      print("La edad es correcta")
else:
      print("la edad es incorrecta")

#...................Ejemplo 2
salario_presidente=int(input("introduce salario presidente: "))
#print("salario presidente: ",salario_presidente) #esta instruccion tambien funciona
print("salario presidente: "+ str(salario_presidente))

salario_director=int(input("introduce salario director: "))
print("salario director: "+ str(salario_director))

salario_Jefe_Area=int(input("introduce salario jefe de area: "))
print("salario jefe Area: "+ str(salario_Jefe_Area))

salario_Administrativo=int(input("introduce salario administrativo: "))
print("salario Administrativo: "+ str(salario_Administrativo))

if salario_Administrativo<salario_Jefe_Area<salario_director<salario_presidente:
      print("todo funciona correctamente")
else:
      print("algo anda mal en esta empresa")
