# 3. Crea una función lambda que devuelva el mayor de dos números.

def numero_mayor():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    mayor = lambda num1, num2: max(num1, num2)
    resultado = mayor(num1, num2)
    print (f"El mayor numero de {num1} y {num2} es {resultado}")

numero_mayor()