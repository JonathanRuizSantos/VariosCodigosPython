from re import A
#-----------------------------------------------------------------------------

print("Hola mundo") #Comentario con Hola mundo
print("Soy un crack")
print("ESTOY PROGRAMANDO PYTHON")
print("esto es genial")
print(4)       #se imprimen numeros de esta manera

#-----------------------------------------------------------------------------
a=4            #las variables crean su tipo automaticamente
print(a)       #Se imprimen variables
print("mi nombre es jonathan")
a='esto es genial x2' # en este caso la variable a es de tipo string y adopto el tipo automaticamente
print(a)          #imprime la variable a de tipo string
#-----------------------------------------------------------------------------
a=0
for i in range(5): # esto es un ciclo for, para i que va de 1 a 5
      a+=1        #a incrementa en 1 
      print(a)    #imprime a

#-----------------------------------------------------------------------------
a=8
type(a)

#-----------------------------------------------------------------------------

                              #para hacer saltos de linea se deben poner una cantidad de "" que indiquen cuantos
                              #saltos de linea de haran
b="""esto es un mensaje
con tres saltos
de linea"""
print(b)

#-----------------------------------------------------------------------------

a=1
b=1.0001
if a>b:                                   #asi se hace un condicional if
      print(a," es mayor que", b)         # se pueden hacer este tipo de cosas, es genial
else:
      print(b," es mayor que", a)

#-----------------------------------------------------------------------------