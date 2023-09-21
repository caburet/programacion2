#Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.


def EsPrimo(numero):
    #Casos especiales que no son primos
    if(numero==0 or numero ==1 or numero == 4) : return False
    for i in range(2,numero -1):
            if numero% i==0:
                return False
    
    return True

   
lista=[numero for numero in range(150) if EsPrimo(numero)]
print(lista)
