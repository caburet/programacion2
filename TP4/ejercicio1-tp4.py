# 1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado.

def cuadrados():
    numero = int(input("Ingrese un número para conocer su cuadrado: "))

    square = lambda numero: numero**2
    resultado = square(numero)
    print(resultado)

cuadrados()