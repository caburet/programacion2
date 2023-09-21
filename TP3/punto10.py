#Dada una lista de números, crea dos listas separadas:
# una que contenga los números pares y otra que contenga los números impares utilizando list comprehensions.

lista_numerica=[1,2,3,4,5,6,7,8,9,10]

lista_par=[numero for numero in lista_numerica if numero%2==0]
lista_impar=[numero for numero in lista_numerica if numero%2!=0]

print("Lista par")
print(lista_par)
print("Lista impar")
print(lista_impar)