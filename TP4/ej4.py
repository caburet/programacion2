#A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.
lista = [1, 2, 3, 4, 5]
incremento = list(map(lambda x:x * 0.15 + x, lista))
print(incremento)