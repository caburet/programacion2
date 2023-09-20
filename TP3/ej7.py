# Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.

def contarPalabras(palabra):
    contador = 0
    vocales = "aeiou"
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

while True:
    palabra = input("ingrese una palabra: ")
    cant_vocales = contarPalabras(palabra)
    if palabra.lower() == 'salir':
        break
    print(f"La palabra {palabra} tiene {cant_vocales} vocales.")