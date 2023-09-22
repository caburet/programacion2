#Crea una función lambda que tome dos números como argumentos y devuelva su suma.
num = int(input("Ingrese 1 numero: "))
num2 = int(input("Ingrese 1 numero: "))

suma = lambda x,y:x + y
print(f"la suma da: {suma(num,num2)}")
