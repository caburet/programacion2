# 7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. 
# El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.

def cantidad_vocales():

    saliendo_programa = True

    while saliendo_programa:
        total_vocales = 0
        palabra = input("Ingrese una palabra, para indicar la cantidad de vocales que tiene la misma/ para salir ingrese 'SALIR': ")
        palabra = palabra.lower()
        if (palabra == "salir"):
            saliendo_programa = False
            print("Saliendo del programa!!! ")
            break
        elif (palabra != "salir"):
            for letra in palabra:
                if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
                    total_vocales = total_vocales + 1
                    saliendo_programa = True
    
        print(f"La palabra {palabra} tiene {total_vocales} vocales")
cantidad_vocales()
