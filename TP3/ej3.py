##3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, utilizando list comprehensions.

##def leer_doc():
  #  line_list = []
   # doc = input("Ingrese el nombre del archivo a leer: ")
   # with open(doc,'r') as archivo:
   #     for linea in archivo:
   #         palabra_limpia = linea.strip()
          #  line_list.append(palabra_limpia)
   # return line_list

#lines = leer_doc()
#print(lines)

line_list = []
doc = "datos.txt"
with open(doc,'r') as archivo:
    line_list = [linea.strip() for linea in archivo]

print(line_list)



