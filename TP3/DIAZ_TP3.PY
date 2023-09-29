def validar_ejercicio():
    numero_ejercio=0
    while numero_ejercio<1 or numero_ejercio>11:
      numero_ejercio=int(input("Ingrese un numero de ejercicio:"))
    return numero_ejercio
    
def menu():
    print("1. Implemente una función que dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.")
    print("2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.")
    print("3. Lee el contenido de un archivo de texto llamado 'datos.txt' y crea una lista con todas las líneas del archivo, utilizando list comprehensions.")
    print("4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica (por ejemplo, 'a') indicada por el usuario, utilizando list comprehensions.")
    print("5. Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.")
    print("6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions.")
    print("7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.")
    print("8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.")
    print("9. Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la multiplicación de los elementos correspondientes de ambas listas utilizando list comprehensions.")
    print("10. Dada una lista de números, crea dos listas separadas: una que contenga los números pares y otra que contenga los números impares utilizando list comprehensions.")
    print("11. Dada una lista de diccionarios que contienen información de estudiantes de una materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos un examen utilizando list comprehensions.")
    

def ejercicio_1():
   lista_original=[1,2,3,4,5,6,7,8,9,10]
   lista_nueva=[]
   lista_nueva=[elemento**2 for elemento in lista_original]
   print("Lista Original")
   print(lista_original)
   print("Lista Nueva")
   print(lista_nueva)

def ejercicio_2():
   lista_nombres=["Jonatan","Bruno","Martina","Gabriel","Cristina","Ana","Marianela","Jose","Pablo","Josefina"]
   cant_caracteres=int(input("Ingrese cantidad de caracteres: "))
   lista_nueva_nombres=[]
   lista_nueva_nombres=[elemento for elemento in lista_nombres if len(elemento)>=cant_caracteres]
   print("Lista Nombres:")
   print(lista_nombres)
   print("Lista Nueva: ")
   print(lista_nueva_nombres)

def ejercicio_3():
   ruta= r"C:\Users\Jona\Desktop\TP3\programacion2\TP3\datos.txt"
   archivo=open(ruta,"r")
   lista_lineas=[]
   lista_lineas=[linea for linea in archivo]
   print("Lista de datos: ")
   print(lista_lineas)

def ejercicio_4():
   letra=input("Ingrese letra:")
   diccionario={"a":1,"ab":2,"abc":3,"b":4,"c":5,"d":6}
   lista_diccionario=[]
   lista_diccionario=[palabra for palabra in diccionario if palabra[0]==letra]
   print("Lista de palabras que comienzan con esa letra: ")
   print(lista_diccionario)


def es_primo(numero):
   contador=0
   for i in range(1,numero+1):
       if numero%i==0:
         contador=contador+1
   if contador==2:
      return True
   else:
      return False
   
def ejercicio_5():
   lista_numeros=list(range(0,101))
   print("Lista numeros:")
   print(lista_numeros)
   lista_primos=[]
   lista_primos=[numero for numero in lista_numeros if es_primo(numero)==True]
   print("Lista primos:")
   print(lista_primos)

def ejercicio_6():
   diccionario={"Jonatan":33,"Bruno":18,"Martina":31,"Gabriel":21,"Cristina":41,"Ana":32,"Marianela":38,"Jose":50,"Pablo":48,"Josefina":25}
   edad=int(input("Ingrese edad: "))
   lista_edad=[]
   lista_edad=[nombre for nombre, valor in diccionario.items() if valor > edad]
   print("Lista de edades: ")
   print(lista_edad)

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra in "aeiou":
			contador += 1
	return contador


def ejercicio_7():
   palabra=""
   while palabra!="salir":
      palabra=input("Ingrese palabras para contar sus vocales, ingrese 'salir' cuando desee finalizar: ")    
      palabra=palabra.lower()
      if palabra!="salir":
          contar=contar_vocales(palabra)
          print(f"La palabra ingresada tiene :{contar}")

def ejercicio_8():
   lista_elementos=[1,1,1,2,3,4,4,5,6,7,7,8,9]
   lista_unica = [numero for numero in lista_elementos if lista_elementos.count(numero) == 1]
   print("Lista completa")
   print(lista_elementos)
   print("Lista sin elementos duplicados") 
   print(lista_unica)

def ejercicio_9():
    lista_1=[1,2,3,4,5,6,7,8,9]
    lista_2=[1,2,3,4,5,6,7,8,9]
    lista_nueva=[]
    lista_nueva=[x * y for x, y in zip(lista_1, lista_2)]
    print("Esta es la lista resultante:")
    print(lista_nueva)

def ejercicio_10():
    lista_numeros=[1,2,3,4,5,6,7,8,9,10]
    lista_impares=[]
    lista_pares=[]
    lista_impares=[numero for numero in lista_numeros if numero%2!=0]
    lista_pares=[numero for numero in lista_numeros if numero%2==0]
    print("Lista pares: ")
    print(lista_pares)
    print("Lista impares:")
    print(lista_impares)

def ejercicio_11():
   diccionario=[{
        'nombre_apellido': 'Juan Pérez',
        'legajo': '001',
        'nota_parcial1': 85,
        'nota_parcial2': 91,
        'nota_final': 88
      },
      {
        'nombre_apellido': 'María López',
        'legajo': '002',
        'nota_parcial1': 78,
        'nota_parcial2': 82,
        'nota_final': 80
      },
      {
        'nombre_apellido': 'Bruno Dahua',
        'legajo': '003',
        'nota_parcial1': 78,
        'nota_parcial2': 95,
        'nota_final': 100
      }
      ]
   lista_nueva=[]
   lista_nueva=[estudiante['nombre_apellido'] for estudiante in diccionario if estudiante['nota_parcial1']>90 or estudiante['nota_parcial2']>90 or estudiante['nota_final']>90]
   print("Lista de alumnos con notas mayor a 90")
   print(lista_nueva)

#Comienzo programa principal

menu()
opcion_ejercico=0
opcion_ejercico=validar_ejercicio()
if opcion_ejercico==1:
   ejercicio_1()
elif opcion_ejercico==2:
   ejercicio_2()
elif opcion_ejercico==3:
   ejercicio_3()
elif opcion_ejercico==4:
   ejercicio_4()
elif opcion_ejercico==5:
   ejercicio_5()
elif opcion_ejercico==6:
   ejercicio_6()
elif opcion_ejercico==7:
   ejercicio_7()   
elif opcion_ejercico==8:
   ejercicio_8()   
elif opcion_ejercico==9:
   ejercicio_9()   
elif opcion_ejercico==10:
   ejercicio_10()  
elif opcion_ejercico==11:
   ejercicio_11()  
