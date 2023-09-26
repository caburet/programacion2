# 4. A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map

def lista_usando_map():
    lista_numeros = [2, 7, 5, 90, 2, 6, 123, 444, 2]

    lista_aumentada = list(map(lambda x: (x * 0.15) + x, lista_numeros))
    print(lista_aumentada)

lista_usando_map()
   


