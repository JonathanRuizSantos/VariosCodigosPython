import pyautogui
from time import sleep

sleep(5)
with open('MensajesBot.txt','r') as file: # Abre el archivo txt
            for line in file:                               # Toma la linea del archivo 
                        pyautogui.typewrite(line)           # Escribe la linea tomada
                        pyautogui.press("enter")
