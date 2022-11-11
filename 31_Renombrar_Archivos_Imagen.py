import cv2
import os

#Direccion de carpeta con mis fotos o imagenes, se debe cambiar la orientacion de el slash
input_images_path = "C:/Users/jon_r/Pictures/FOTOS/Mis Fotos"

# Obtencion de una lista con todos los archivos dentro de esa direccion
files_names = os.listdir(input_images_path)
print(files_names)
print()

# Creacion de una carpeta que guardara nuevas imagenes de este script
output_images_path = "C:/Users/jon_r/Pictures/FOTOS/Mis_Fotos_jpg"

# Si la carpeta anterior no existe se crea
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)
    print()

# contador para el numero de foto
count = 0

# Procesamiento de imagenes
for file_name in files_names:
    #print(file_name)
    '''
    # Filtro que solo tomara en cuenta las extenciones seleccionadas
    if file_name.split(".")[-1] not in ["jpeg", "png"]:
        continue
    '''
    image_path = input_images_path + "/" + file_name
    print(image_path)                                       #Imprime la direccion de cada una de las imagenes

    # Lee cada uno de los archivos
    image = cv2.imread(image_path)

    # si el archivo leido no es una imagen se lo salta
    if image is None:
        continue
    '''
    # Procesamiento de las imagenes
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)
    '''
    
    # Guarda cada una de las imagenes en la carpeta creada anteriormente
    cv2.imwrite(output_images_path + "/image" + str(count) + ".jpg", image)
    count += 1

    '''
    # Muestra cada una de las imagenes durante el proceso
    cv2.imshow("Image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
'''