#Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.

new_list = []
list_comprenhension = []
def EsPrimo():
    for numero in range(1,10):
        if numero != 1:
            if numero == 2 or numero % 2 == 1:
                new_list.append(numero)
    return new_list

print(f"Normal: {EsPrimo()}")     

list_comprenhension = [ numero for numero in range(1,10) if numero != 1 if numero == 2 or numero % 2 == 1]

print(f"List comprenhension: {list_comprenhension}")