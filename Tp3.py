from os import system

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
    print("------------------------")
    if opcion == "0":
        print("Saliendo...")
        sigue = False  

    elif opcion == "1":
        print("1 - Ejercicio")
        #Ej_1()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "2":
        print("2 - Ejercicio")
        #Ej_2()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "3":
        print("3 - Ejercicio")
        #Ej_3()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "4":
        print("4 - Ejercicio")
        #Ej_4()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "5":
        print("5 - Ejercicio")
        #Ej_5()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "6":
        print("6 - Ejercicio")
        #Ej_6()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "7":
        print("7 - Ejercicio")
        #Ej_7()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "8":
        print("8 - Ejercicio")
        #Ej_8()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "9":
        print("9 - Ejercicio")
        #Ej_9()
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    else:
        print("Opcion incorrecta, pruebe de vuelta")
