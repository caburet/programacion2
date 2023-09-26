#Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, 
#utilizando list comprehensions.

def cargar_lista():
    ruta = "C:\\Users\\camal\\OneDrive\\Desktop\\Instaladores de apps\\PROGRAMACION II\\MI_programacion2\\TP3\\datos.txt"
    with open(ruta, 'r') as archivo:
        lista_archivo = [linea.strip() for linea in archivo.readlines()]
        print(lista_archivo)

cargar_lista()

    
