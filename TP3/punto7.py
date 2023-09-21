#Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.

def ContarVocales(palabra):
    contador=0
    for vocal in palabra:
        if vocal=='a'or vocal=='e' or vocal=='i' or vocal == 'o' or vocal == 'u':
            contador+=1
    return contador
palabra=''
while palabra!='salir':
    palabra=input("Ingrese una palabra, ingrese 'salir' para cerrar el programa ").lower()
    contador=ContarVocales(palabra)
    print(f"La palabra {palabra} contiene {contador} vocales")

