# Dada una lista de números, crea dos listas separadas: una que contenga los números pares y otra que contenga los números impares utilizando list comprehensions

lista_completa = [1,2,3,4,5,6,7,8,9,10]

def DividirLista(lista_completa):
    list_par = []
    list_impar = []
    for num in lista_completa:
        if num % 2 == 0:
            list_par.append(num)
        elif num % 2 == 1:
            list_impar.append(num)
    return list_impar, list_par

listaImpar, listaPar = DividirLista(lista_completa)
print(f"La lista par es: {listaPar} y la impar es {listaImpar}")
print ("list comprehension: ")
list_par1 = [num for num in lista_completa if num % 2 == 0]
list_impar1 = [num for num in lista_completa if num % 2 == 1]
print(f"La lista par es: {list_par1} y la impar es {list_impar1}")

