import random
import string

boleano = True
while boleano:
            caracteres = string.ascii_letters + string.digits + '#$&%'
            word = ""
            n = int(input("Ingresa la cantidad de caracteres: "))
            for i in range(n):
                        letra_Aleatoria = random.choice(caracteres)
                        word += letra_Aleatoria

            print(word)