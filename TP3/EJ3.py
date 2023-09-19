#3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, 
#   utilizando list comprehensions.

arch_datos =open('G:/Mi unidad/Programacion/UTN/Programacion2/TP-3/programacion2/TP3/datos.txt','r')

def cargar_lista(archivo):
    lista_archivo = [linea.strip().split(';') for linea in archivo]
    return lista_archivo


print(cargar_lista(arch_datos))
arch_datos.close()