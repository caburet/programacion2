#Crea una función lambda que devuelva el mayor de dos números.
num = int(input("Ingrese 1 numero: "))
num2 = int(input("Ingrese 1 numero: "))

mayor = lambda x,y: True if x > y else False

if mayor == True:
    print(f"el numero {num} es mayor a {num2}")
else:
    print(f"el numero {num2} es mayor a {num}")
 