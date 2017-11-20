import os
from os.path import isfile, join, isdir, splitext
from os import listdir

def cambiar_ext(path, ext):
    path = safe_path(path)
    ext = safe_ext(ext)

    if isdir(path):
        for file in listdir(path):
            if isfile(join(path, file)):
                base = splitext(file)[0]
                os.rename(path + file, path +  base + ext)
        return "Listo"
    else:
        return path + " no es un directorio válido"

def safe_path(path):
    path += "\\"
    return path

def safe_ext(ext):
    ext = ext.replace(".", "")
    ext = "." + ext
    return ext

def main():
    path = input("Ingrese la ruta absoluta del directorio que contiene los archivos: ")
    ext = input("A que extension quiere cambiar: ")

    print(cambiar_ext(path, ext))

main()
