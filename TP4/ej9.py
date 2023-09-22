#Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras

palabras = ['manzana', 'banana', 'naranja', 'pera', 'uva', 'sandía', 'kiwi', 'cereza', 'fresa', 'melón']

def Lista_Ord(palabras):
    nuevalista = list(sorted(palabras, key=lambda x:len(x)))
    return nuevalista


print(Lista_Ord(palabras))