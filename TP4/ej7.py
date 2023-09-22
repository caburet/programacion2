#7. Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.

lista = [1, 2, 3, 4, 5,6,7,8,9,10]
def par(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

def parCorto(lista):
    Lista_par = list(filter(lambda x: x % 2 == 0, lista))
    return Lista_par


print(f"forma comun: {par(lista)}")
print(f"forma corta: {parCorto(lista)}")
