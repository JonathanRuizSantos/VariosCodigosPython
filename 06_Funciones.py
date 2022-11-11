#sintaxis de las funciones 

#-----------------------------------------------------------------------------------------ejemplo 1
def nombre():                 #aqui se muestra la sintaxis de la declaracion de una funcion o metodo
      nom="Jonathan R.S."
      print(nom)              #esta funcion imprime lo que hay en la variable nom que es de tipo string en este caso

nombre()

#-----------------------------------------------------------------------------------------ejemplo 2
def persona(nombre, Apaterno, Amaterno):              #Aqui se uso una funcion con parametros en el argumento
                                                      #estas funciones sirven para poder cambiar los parametros
                                                      #mas facil desde la misma funcion
      print("Programa: cual es tu nombre? ")    
      print("Usuario: ",nombre)
      print("Programa: cual es tu apellido paterno? ")
      print("Usuario: ",Apaterno)
      print("Programa: cual es tu apellido materno? ")
      print("Usuario: ",Amaterno)

persona("Jonathan","Ruiz","Santos")             #aqui se estan imprimiento diferentes nombres de personas
persona("Carlos","Pacheco","Luna")              #haciendo uso de una misma funcion para los tres casos
persona("Rodrigo","Reyes","Acosta")
#------------------------------------------------------------------------------------------------
#ejemplo 3
def suma(num1,num2):                  #Esta es una funcion que recibe dos argumentos y devuelve un valor
      total=num1+num2
      return total
S=suma(6,8)
print("suma es igual a: ",S)

