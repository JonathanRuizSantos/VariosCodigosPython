print("programa de evaluacion de notas de alumnos")

nota_alumno=input() #esta instruccion dara un error a proposito

def evaluacion(nota):
      valoracion="aprobado"
      if nota<5:
            valoracion="suspenso"
      return valoracion


#print(evaluacion(4)) # es una nota fija
print(evaluacion(int(nota_alumno)))  #la nota ahora se instroduce por teclado, ya no es fija
