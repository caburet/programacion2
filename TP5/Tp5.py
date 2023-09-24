from os import system
import random

global separador
separador = "------------------------"

def MainMenu():
    print("********************") 
    print("**  1 - Ejercicio **")
    print("**  2 - Ejercicio **")
    print("**  3 - Ejercicio **")
    print("**  4 - Ejercicio **")
    print("**  5 - Ejercicio **")
    print("**  6 - Ejercicio **")
    print("**  7 - Ejercicio **")
    print("**  8 - Ejercicio **")
    print("**  0 - Salir     **")
    print("********************")

#Colas

def encolar(elemento, cola):
    return cola.append(elemento)

def desencolar(cola):
    if not esta_vacia_cola(cola):
        return cola.pop(0)
    else:
        return print("La cola esta vacia")
    
def longitud_cola(cola):
    return len(cola)

def esta_vacia_cola(cola):
    return len(cola) == 0

def Ej_1():
    cola = []
    encolar(2, cola)
    encolar(6, cola)
    encolar(10, cola)
    encolar(11, cola)
    #console: 2, 6, 10, 11
    desencolar(cola)
    #console: 6, 10, 11
    encolar(5, cola)
    #console: 6, 10, 11, 5
    desencolar(cola)
    desencolar(cola)
    #console: 11, 5

    print(f"La longitud: {longitud_cola(cola)}")

    print(f"resultado: {cola}")

#Pilas

def apilar(elemento, pila):
    pila.append(elemento)

def desapilar(pila):
    if not esta_vacia_pila(pila):
        return pila.pop()
    else:
        return print("La pila esta vacia")

def longitud_pila(pila):
    return len(pila)

def esta_vacia_pila(pila):
    return len(pila) == 0

def Ej_2():
    pila = []
    apilar(11, pila)
    apilar(321, pila)
    apilar(10, pila)
    # 11, 321, 10
    desapilar(pila)
    apilar(12, pila)
    # 11, 321, 12
    desapilar(pila)
    desapilar(pila)
    # 11
    apilar(33, pila)
    apilar(30, pila)
    # 11, 33, 30
    print(f"Longitud: {longitud_pila(pila)}")
    print(f"Resultado: {pila}")

def generar_lista_random():
    #Agrega a la lista numeros entre 200 y 5000, con una longitud de 20 y 50 de elementos 

    lista = [random.randint(200, 5000) for i in range(random.randint(20, 50))]
    
    return lista

def Ej_3():
    #3. Usando el módulo random, cree ua función que retorne dos listas de longitud aleatoria entre 20 y 50, 
    #   y cada lista con elementos de valores aleatorios entre 200 y 5000.
    
    lista1 = generar_lista_random()
    lista2 = generar_lista_random()

    print("La lista numero uno tiene estos valores: ")
    print(lista1)
    print(len(lista1))
    print(separador)
    print("La lista numero dos tiene estos valores: ")
    print(lista2)
    print(len(lista2))

def generar_lista_impares(lista):

    numeros_impares = list(filter(lambda x: x % 2 != 0, lista))

    return numeros_impares

def es_primo(n):
    for i in range(2 , n):
        if  n % i == 0:
            return False
        
    return True

def Ej_4(): 
    #4. Utilizando la función anterior genere dos listas de datos. Con la lista1 se debe generar una sublista 
    #   con los elementos impares de lista1 multiplicados por el valor menor de la lista2.
    #   Con la lista2 se debe devolver el menor número primo contenido en la lista, o “-1” si no tiene números primos.
    #Gero listas random
    lista1 = generar_lista_random()
    lista2 = generar_lista_random()
    
    #Ordeno lista para encontrar el menor de esta misma
    lista2_ordenada = sorted(lista2)
    menor_lista2 = lista2_ordenada[0]

    #Creo sublista de impares de la lista1 
    impares_lista1 = generar_lista_impares(lista1)

    #Con list comprehesion multiplico los valores de los impares al numero menor de la lista2
    lista_multiplicados = list(map(lambda x: x * menor_lista2, impares_lista1))

    #resultado
    print("La lista de multiplicados de la lista1 por el valor menor de la lista 2 es: ")
    print(lista_multiplicados)
    
    #sublista para los primos de la lista2
    primos_lista2 = list(filter(lambda x: es_primo(x), lista2_ordenada))

    print(f"El Menor numero primo de la lista dos es {primos_lista2[0]}") if len(primos_lista2) > 0 else print("No hay numeros primos en la lista")

def Ej_5():
    print('hola')
#Main
sigue = True

while (sigue):

    MainMenu()
    opcion = input("Ingrese una opcion: ")
    print(separador)
    if opcion == "0":
        print("Saliendo...")
        sigue = False  

    elif opcion == "1":
        print("1 - Ejercicio")
        print(separador)
        Ej_1()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "2":
        print("2 - Ejercicio")
        print(separador)
        Ej_2()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "3":
        print("3 - Ejercicio")
        print(separador)
        Ej_3()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "4":
        print("4 - Ejercicio")
        print(separador)
        Ej_4()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "5":
        print("5 - Ejercicio")
        print(separador)
        #Ej_5()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "6":
        print("6 - Ejercicio")
        print(separador)
        #Ej_6()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

