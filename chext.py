import os
from os.path import isfile, join, isdir
from os import listdir


def main():
    path = input("Ingrese la ruta absoluta del directorio que contiene los archivos: ")
    if isdir(path):
        path = path + "\\"
        ext = input("A que extension quiere cambiar: ")
        ext = "." + ext
        for file in listdir(path):
            if isfile(join(path, file)):
                base = os.path.splitext(file)[0]
                os.rename(path + file, path +  base + ext)

        print("Listo!")
    else:
        print ("La ruta no apunta a un directorio válido")

def isdir(path):
    if os.path.isdir(path):
        return True
    else:
        return False

main()
