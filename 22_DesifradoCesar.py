# PROGRAMA DE DESCIFRADO CESAR SIN CLAVE

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrado = "LZAL SLTZHPL LZ JOMYHKV"

for clave in range(1, len(alfabeto)):
            mensaje = ""
            for letra in cifrado.upper(): #Para poner el mensaje en mayusculas
                        if letra in alfabeto:
                                    indice = alfabeto.find(letra)
                                    indice -= clave
                                    if indice < 0:
                                                indice += 27
                                    mensaje += alfabeto[indice]
                        else:
                                    mensaje += letra
            print(f"Clave:{clave} - {mensaje}")