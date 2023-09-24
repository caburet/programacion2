from functools import reduce
#13. Encuentra el número mayor de una lista utilizando reduce.
numeros = [13, 21, 356, 434, 45, 64 ,27, 8, 91, 103, 113, 142]

def Func_menor(x,y):
    if x < y:
        return x
    else:
        return y

menor = reduce(Func_menor,numeros)
print(f"El numero mas chicos es: {menor}")