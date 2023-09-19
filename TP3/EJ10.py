#10. Dada una lista de números, crea dos listas separadas: una que contenga los números pares y otra que contenga
#    los números impares utilizando list comprehensions.

lista =[1,2,3,4,5,6,7,8,9]

lista_pares = [item for item in lista if item%2==0]
lista_impares = [item for item in lista if item%2!=0]

print("Pares: ", lista_pares)
print("Impares: ", lista_impares)