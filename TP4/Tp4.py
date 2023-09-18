from os import system
from functools import reduce
import os 
global separador
separador = "------------------------"

#Funciones extras
def numero_valido(texto):
    while True: 
        try:
            numero = int(input(texto))
            
            print(separador)
            return numero
        except ValueError:
            print(separador)
            print("Eso no es un número entero válido. Inténtalo de nuevo.")
            print(separador)

def Ej_1():
    #1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado. 
    texto = "Escriba el numero que quiere elevar al cuadrado: "
    cuadrado = lambda x: x**2

    numero = numero_valido(texto)

    print(f"El numero {numero} al cuadrado es: {cuadrado(numero)}")


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
    print("**  9 - Ejercicio **")
    print("** 10 - Ejercicio **")
    print("** 11 - Ejercicio **")   
    print("**  0 - Salir     **")
    print("********************")

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
        #Ej_2()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "3":
        print("3 - Ejercicio")
        print(separador)
        #Ej_3()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "4":
        print("4 - Ejercicio")
        print(separador)
        #Ej_4()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "5":
        print("5 - Ejercicio")
        print(separador)
        #Ej_5()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "6":
        print("6 - Ejercicio")
        print(separador)
        #Ej_6()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "7":
        print("7 - Ejercicio")
        print(separador)
        #Ej_7()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "8":
        print("8 - Ejercicio")
        print(separador)
        #Ej_8()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "9":
        print("9 - Ejercicio")
        print(separador)
        #Ej_9()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")
    elif opcion == "10":
        print("10 - Ejercicio")
        print(separador)
        #Ej_10()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")
    elif opcion == "11":
        print("11 - Ejercicio")
        print(separador)
        #Ej_11()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    else:
        print("Opcion incorrecta, pruebe de vuelta")
