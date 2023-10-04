def MainMenu(ejercicios):
    print("********************") 
    for num in range(ejercicios):
        if len(str(num)) == 1:
            print(f"**  {num} - Ejercicio **")
        else:
            print(f"** {num} - Ejercicio **")
    print("********************")

def main(ejercicios):
    sigue = True
    separador = "********************"

    while (sigue):
        palabra = "Ej_"
        MainMenu(ejercicios)
        opcion = input("Ingrese una opcion: ")
        print(separador)
        if opcion == "0":
            print("Saliendo...")
            sigue = False 
            break 

        for num in range(ejercicios + 1 ):
            indice = num + 1
            aux = str(indice)
            palabra += aux
            
            if opcion == indice:
                print(f"{num} - Ejercicio")
                print(separador)
                
                    


        
        
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

        else:
            print("Opcion incorrecta, pruebe de vuelta")