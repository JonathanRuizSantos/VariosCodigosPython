'''
ACERCA DE:
PROGRAMA QUE COMPRIME IMÁGENES, SE PRESENTA UN MENÚ CON OPCIONES ENTRE LAS QUE PUEDES ELEGIR QUE HACER

FECHA DE INICIO DE CODIFICACIÓN: 31/10/2022
FECHA DE ULTIMA MODIFICACION AL CÓDIGO: 01/11/2022
ESTADO: CMPLETO Y FUNCIONAL

COMPUTECH, JONATHAN RS.
'''
from PIL import Image
import cv2
import os
from os import system

# ----------------------------------------------------------------------------------------------- FUNCIONES
def menu():
            print("********** MENÚ DE OPCIONES **********")
            print("--------------------------------------")
            print("(1) Comprimir solo una imágen")
            print("(2) Comprimir colección de imagenes")
            print("(3) Renombrar archivos tipo imágen de una carpteta")
            print("(4) Salir")
            print("")
            opcion = int(input('Yo elijo la opción: '))
            return opcion

def menuRepetir():
            opcion = int(input("Presiona 1 para ir a menú y 2 para salir: "))
            return opcion

def direcciones():
            carpetaFuente = input("Ingresa la dirección fuente con diagonales invertidas: ")
            return carpetaFuente

def comprimeGuardaImagen(imgFoder,imgName):
            
            name, extension = os.path.splitext(imgFoder + imgName)

            if extension in [".jpg", ".jpeg", ".png"]:
                        picture = Image.open(imgFoder + imgName)
                        picture.save(imgFoder + "compressed_"+ imgName, optimize=True, quality=60)
                        os.remove(imgFoder + imgName)
                        print("--------------------------------------------------------------")
                        print(name + ": " + extension)

def comprimeGuardaEliminaMismoFolder(imgFoder):
            if __name__ == "__main__":
                        for filename in os.listdir(imgFoder):
                                    name, extension = os.path.splitext(imgFoder + filename)

                                    if extension in [".jpg", ".jpeg", ".png"]:
                                                picture = Image.open(imgFoder + filename)
                                                #picture.save(imgFoder + "compressed_"+filename, optimize=True, quality=60)
                                                picture.save(imgFoder + "compressed_"+filename, optimize=True, quality=60)
                                                os.remove(imgFoder + filename)
                                                print("--------------------------------------------------------------")
                                                print(name + ": " + extension)

def RenombrarSinExtensiones_MismaCarpeta(count, files_names, input_images_path):
    for file_name in files_names:
        # Imprime la direccion de cada una de las imagenes
        image_path = input_images_path + "/" + file_name
        print(image_path) 

        # Lee cada uno de los archivos
        image = cv2.imread(image_path)

        # si el archivo leido no es una imagen se lo salta
        if image is None:
            continue

        # Guarda cada una de las imagenes en la carpeta creada anteriormente
        cv2.imwrite(input_images_path + "/imagen" + str(count) + ".jpg", image)
        os.remove(input_images_path + "/" + file_name)
        count += 1

# ---------------------------------------------------------------------------------------------- PROGRAMA PRINCIPAL
print("")
print("*************************************************************************************************************")
print("PROGRAMA QUE COMPRIME IMÁGENES. SE PRESENTAN DIFERENTES OPCIONES ENTRE LAS QUE PUEDES ELEJIR LA DE TU AGRADO")
print("VERSION 22.1")
print("")

opcionRepetir = 1
while (opcionRepetir == 1):
            opcion = menu()
            print("")
            if opcion == 1:
                        system("cls")
                        print("**************** COMPRESOR DE UNA IMAGEN *********************")
                        print("--------------------------------------------------------------")
                        print("Ejemplo de entrada: C:/Users/jon_r/Pictures/FOTOS/Mis Fotos/")
                        print("--------------------------------------------------------------")
                        carpetaFuente = direcciones()
                        imgName = input("Ingresa el nombre de la imágen a comprimir: ")
                        comprimeGuardaImagen(carpetaFuente,imgName)
                        print("--------------------------------------------------------------")
                        print("\n PROCESO TERMINADO SATISFACTORIAMENTE\n")

            elif opcion == 2:
                        system("cls")
                        print("**************** COMPRESOR DE UNA IMAGEN *********************")
                        print("--------------------------------------------------------------")
                        print("Ejemplo de entrada: C:/Users/jon_r/Pictures/FOTOS/Mis Fotos/")
                        print("--------------------------------------------------------------")
                        carpetaFuente = direcciones()
                        comprimeGuardaEliminaMismoFolder(carpetaFuente)
                        print("--------------------------------------------------------------")
                        print("\n PROCESO TERMINADO SATISFACTORIAMENTE\n")
            
            elif opcion == 3:
                        system("cls")
                        print("************* RENOMBRAR IMAGENES EN CARPETA ******************")
                        print("--------------------------------------------------------------")
                        print("Ejemplo de entrada: C:/Users/jon_r/Pictures/FOTOS/Mis Fotos")
                        print("--------------------------------------------------------------")
                        carpetaFuente = direcciones()
                        print("\n--------------------------------------------------------------")
                        # Obtencion de una lista con todas las imagenes en la carpeta fuente
                        files_names = os.listdir(carpetaFuente)
                        print(files_names)
                        print("--------------------------------------------------------------")
                        count = 0
                        RenombrarSinExtensiones_MismaCarpeta(count, files_names, carpetaFuente)
                        print("--------------------------------------------------------------")
                        print("\nPROCESO TERMINADO SATISFACTORIAMENTE\n")

            elif opcion == 4:
                        system("cls")
                        exit()
            else:
                        system("cls")
                        print("OPCION NO DISPONIBLE")

            print("\n--------------------------------------------------------------\n")
            opcionRepetir = menuRepetir()
            system("cls")

system("cls")
print("PROGRAMA TERMINADO, ¡¡¡NOS VEMOS PRONTO!!!")
print("")
system("pause")