def MainMenu(ejercicios):
    print("********************") 
    for num in range(ejercicios):
        if len(str(num)) == 1:
            print(f"**  {num} - Ejercicio **")
        else:
            print(f"** {num} - Ejercicio **")

    print("********************")
