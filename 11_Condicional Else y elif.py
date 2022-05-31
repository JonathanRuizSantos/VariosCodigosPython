print("verificacion de acceso")

#EJEMPLO 1
edad_usuario=int(input("introduce tu edad, por favor:  "))

if edad_usuario<18:
      print("no puedes pasar")

elif edad_usuario>100:
      print("la edad no es aceptable")
else:
      print("puedes pasar")

print("el programa ha finalizado")

#EJEMPLO 2

nota_usuario=int(input("introduce tu nota, por favor:  "))

if nota_usuario<=5:
      print("insuficiente")

elif nota_usuario<=6:
      print("suficiente")

elif nota_usuario<=7:
      print("bien")

elif nota_usuario<=9:
      print("notable")

else:
      print("sobresaliente")

print("el programa ha finalizado")