# 10. Dada una lista de números, crea dos listas separadas: una que contenga los números pares
# y otra que contenga los números impares utilizando list comprehensions.

def numeros():
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    lista_pares = [num for num in lista_numeros if num%2 == 0]
    lista_impares = [num for num in lista_numeros if num% 2 != 0]

    print(lista_pares)
    print(lista_impares)

numeros()