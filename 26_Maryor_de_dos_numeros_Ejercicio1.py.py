numero_1=int(input("Dame el primer numero brother: "))
numero_2=int(input("Dame un segundo numero brother, porfa: "))

def DevuelveMax():
      if numero_1<numero_2:
            print(numero_2, " es mayor que ", numero_1)
      elif numero_1>numero_2:
            print(numero_1, " es mayor que ", numero_2)
      else:
            print("Ambos numeros son iguales")

numero_1
numero_2
DevuelveMax()
