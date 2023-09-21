#Lee el contenido de un archivo de texto llamado "texto.txt" y 
#crea una lista con todas las líneas del archivo, utilizando list comprehensions.

def LeerArchivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            lista = [linea.strip() for linea in file]    
            return lista
    except FileNotFoundError:
        print("No se ha encontrado el archivo")

nombre_archivo = "texto.txt"
lista = LeerArchivo(nombre_archivo)
print(lista)
