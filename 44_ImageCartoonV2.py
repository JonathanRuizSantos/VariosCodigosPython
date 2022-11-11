'''
## Cartoonizacion de una imagen

* FECHA DE INICIO DE CODIFICACION 01/11/22
* ULTIMA EDICION AL CODIGO: 01/11/22
* ESTADO: SIN TERMINAR Y SIN FUNCIONAR
'''

# Importar librerias
import cv2
import numpy as np
from os import system

print("\n***********************************************************************************\n")

print("********************** Programa que Cartooniza una imagen *****************************\n")
print("Ejemplo de entrada: C:/Users/jon_r/Pictures/FOTOS/Mis Fotos/image10.jpg\n")

imagen = input("Ingresa la direccion con las diagonales investidas: ")

# reading image
img = cv2.imread(imagen)

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Cartoonizacion
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

'''
cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
'''
cv2.imwrite("edges.jpg", edges)
cv2.imwrite("Cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\n********************* PROCESO TERMINADO SATISFACTORIAMENTE **************************'\n")

system("pause")