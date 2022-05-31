#CONDICIONAL IF CON OPERADORES AND Y OR
"""print("programa de becas año 2022")
distancia_escuela=int(input("introduce la distancia a la escuela en km:  "))
print(distancia_escuela)

numero_hermanos=int(input("introduce el numero de hermanos en el centro:  "))
print(numero_hermanos)

salario_familiar=int(input("introduce salario anuario bruto:  "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
      print("tienes derecho a beca")
else:
       print("no tienes derecho a beca")"""

#--------------------------------------------------------------------------------------------------

#OPERADORES IN
print("Asignaturasoptativas año 2022")
print("Asignaturas optaticas: Informatica grafica - pruebas de software - Usabilidad y accesibilidad")
opcion=input("escribe la asignatura escogida:  ")

asignatura=opcion.lower() #lower() transforma las mayusculas a minusculas

if asignatura in ("Informatica grafica", "Pruebas de software", "Usabilidad y accsesibilidad"):
      print("Asignatura elegida" + asignatura)
else:
      print("la asignatura escogida no esta contemplada")

#lower() transforma las mayusculas a minusculas
#upper() transforma las minusculas a mayusculas