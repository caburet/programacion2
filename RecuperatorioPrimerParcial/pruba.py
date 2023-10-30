def suma_caracteres(cadena):
    suma = 0
    for caracter in cadena:
        suma += ord(str(caracter))
    return suma

print(suma_caracteres("adawd"))