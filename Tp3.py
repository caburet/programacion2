from os import system

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

def obtener_num_mayor_0(texto):

    while True: 
        try:
            numero = int(input(texto))
            if numero > 0:
                print(separador)
                return numero
            else:
                print(separador)
                print("El numero tiene que ser mayor a 0")
                print(separador)
        except ValueError:
            print(separador)
            print("Eso no es un número entero válido. Inténtalo de nuevo.")
            print(separador)

#Ejercicio 1

def Ej_1():
    #1. Implemente una función que dada una lista de números, devuelva una nueva lista que contenga 
    #   el cuadrado de cada número utilizando list comprehensions.
    print("En este ejericio tiene que agregar la cantidad de numeros que queres ")
    print("y todos los numeros ingresados va ser elevado por 2")
    print(separador)

    texto_repeticion = "Ingrese la cantidad de numero que quiere ingresar: "
    
    repeticion = obtener_num_mayor_0(texto_repeticion)
    lista = []
    lista = [numero_valido(f"Ingrese numero {i + 1}°: ") for i in range(repeticion)]
    
    lista_elevada = [num**2 for num in lista]
    print(lista)
    print(lista_elevada)

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
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "2":
        print("2 - Ejercicio")
        #Ej_2()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "3":
        print("3 - Ejercicio")
        #Ej_3()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "4":
        print("4 - Ejercicio")
        #Ej_4()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "5":
        print("5 - Ejercicio")
        #Ej_5()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "6":
        print("6 - Ejercicio")
        #Ej_6()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "7":
        print("7 - Ejercicio")
        #Ej_7()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "8":
        print("8 - Ejercicio")
        #Ej_8()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "9":
        print("9 - Ejercicio")
        #Ej_9()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    else:
        print("Opcion incorrecta, pruebe de vuelta")
