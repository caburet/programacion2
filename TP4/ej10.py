#10. Dada una lista de palabras, generar una lista con las iniciales de cada palabra.

palabras = ['manzana', 'banana', 'naranja', 'pera', 'uva', 'sandía', 'kiwi', 'cereza', 'fresa', 'melón']

def Iniciales(palabras):
    iniciales = [palabra[0] for palabra in palabras]
    return iniciales

print(Iniciales(palabras))