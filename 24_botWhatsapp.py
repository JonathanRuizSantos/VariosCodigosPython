import pyautogui, webbrowser
from time import sleep

webbrowser.open('http://web.whatsapp.com/send?phone=+5215535966450') #Abre el enlace de whatsapp

sleep(10)    #Tiempo de espera

with open('MensajesBot.txt','r') as file: # Abre el archivo txt
            for line in file:                               # Toma la linea del archivo 
                        pyautogui.typewrite(line)           # Escribe la linea tomada
                        pyautogui.press("enter")            # Envia la linea tomada