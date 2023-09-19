#7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella.
#    El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.


continuar = True

while continuar:
    contador = 0
    palabra = input("ingrese una palabra('salir') para salir: ")
    palabra.lower()
    if palabra =='salir':
        print("Terminando..")
        continuar = False
        break
    else:
        for letra in palabra:
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                contador += 1
    print(f"La palabra tiene {contador} vocales")
