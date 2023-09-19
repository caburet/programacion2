#5. Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.

lista_numeros = [1,2,3,4,5,6,7,8,9]

def es_primo(numero):
    contador = 0
    for i in range(1, numero+1):
        if numero % i == 0 :
            contador += 1

    if contador == 2:
        return True
    else:
        return False

def lista_de_primos(lista):
    nueva_lista =[valor for valor in lista if es_primo(valor)]
    return nueva_lista

print(lista_de_primos(lista_numeros))