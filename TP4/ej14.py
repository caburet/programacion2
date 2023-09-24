from functools import reduce
#14. Utilice reduce para concatenar una lista de cadenas en una sola cadena
palabras = ['manzana', 'banana', 'naranja', 'pera', 'uva', 'sandía', 'kiwi', 'cereza', 'fresa', 'melón']

newpalabra = reduce(lambda x,y: x + y, palabras) #Se puede usar newpalabra = "".join(palabras) y las une 
print(newpalabra)