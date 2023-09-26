# 2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.

def suma_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    suma = lambda num1, num2: (num1 + num2)
    resultado = suma(num1, num2)

    print(f"El resultado de la suma es: {resultado}")

suma_numeros() 
