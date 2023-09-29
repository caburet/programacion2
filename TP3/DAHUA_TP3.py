def validar_ejercicio():
    numero_ejercicio=-1
    while numero_ejercicio<0 or numero_ejercicio>11:
        numero_ejercicio=int(input("\nIngrese un numero de ejercicio: "))
    return numero_ejercicio

def menu():
    print("\n0 SALIR")
    print("\n1 Implemente una función que dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando listas por comprensión.")
    print("\n2 Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasados por parámetro, utilizando listas por comprensión.")
    print("\n3 Lee el contenido de un archivo de texto llamado 'datos.txt' y crea una lista con todas las líneas del archivo, utilizando listas por comprensión.")
    print("\n4 Dado un diccionario de palabras y sus definiciones, crea una lista que contiene sólo las palabras que comienzan con una letra específica (por ejemplo, 'a') indicada por el usuario, utilizando listas de comprensión.")
    print("\n5 Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando listas por comprensión.")
    print("\n6 Dado un diccionario de personas y sus edades, crea una lista que contiene solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando listas por comprensión.")
    print("\n7 Implemente un programa que le pide una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra 'salir'.")
    print("\n8 Dada una lista con elementos duplicados, crea una nueva lista que contiene solo los elementos únicos utilizando listas por comprensión.")
    print("\n9 Dadas dos listas de números del mismo tamaño, crea una nueva lista que contiene la multiplicación de los elementos correspondientes de ambas listas utilizando listas por comprensión.")
    print("\n10 Dada una lista de números, crea dos listas separadas: una que contiene los números pares y otra que contiene los números impares utilizando listas por comprensión.")
    print("\n11 Dada una lista de diccionarios que contienen información de estudiantes de una materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contiene los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos un examen utilizando enumerar comprensiones.")

def ejercicio_uno():
    lista_original=[1,2,3,4,5,6,7,8,9,10]
    print(f"\nEsta es la lista original: {lista_original}")
    lista_nueva=[]
    lista_nueva=[elemento**2 for elemento in lista_original]
    print(f"\nEsta es la lista nueva: {lista_nueva}")

def ejercicio_dos():
    cant_caracteres=int(input("\nIngrese cantidad de caracteres: "))
    lista_nombres=["Bruno","Jonatan","Martina","Gabriel","Cristina","Ana","Marianella","Jose","Pablo","Josefina"]
    print(f"\nEsta es la lista original: {lista_nombres}")
    lista_nueva_nombres=[]
    lista_nueva_nombres=[elemento for elemento in lista_nombres if len(elemento)>=cant_caracteres]
    print(f"\nEsta es la lista nueva: {lista_nueva_nombres}")

def ejercicio_tres():
    ruta= r"C:\Users\Windows10\Desktop\UTN\Prog II\TP3\datos.txt"
    archivo=open(ruta, "r")
    lista_lineas=[]
    lista_lineas=[linea for linea in archivo]
    print(f"\nEsta es la lista de datos: {lista_lineas}")

def ejercicio_cuatro():
    letra=input("\nIngrese letra: ")
    diccionario={"a":1,"ab":2,"abc":3,"abcd":4}
    lista_diccionario=[]
    lista_diccionario=[palabra for palabra in diccionario if palabra[0]==letra]
    print(f"\nEsta es la lista con {letra}: {lista_diccionario}")

def ejercicio_cinco():
    lista_numeros=list(range(0,101))
    print(lista_numeros)
    lista_primos=[]
    lista_primos=[numero for numero in lista_numeros if es_primo(numero)==True]
    print(f"\nEsta es la lista de numeros primos: {lista_primos}")
    
def es_primo(numero):
   contador=0
   for i in range(1,numero+1):
       if numero%i==0:
         contador=contador+1
   if contador==2:
      return True
   else:
      return False

def ejercicio_seis():
    diccionario={"Bruno":18,"Jonatan":33,"Martina":30,"Gabriel":50,"Cristina":41,"Ana":10,"Marianella":200,"Jose":40,"Pablo":48,"Josefina":12}
    edad=int(input("\nIngrese edad:"))
    lista_edades=[]
    lista_edades=[nombre_persona for nombre_persona, edad_persona in diccionario.items() if edad_persona > edad]
    print(f"\nEsta es la lista de edades menores a {edad} : {lista_edades}")

def ejercicio_siete():
    palabra=""
    while palabra!="salir":
        palabra=input("\nIngrese palabra ('salir' para finalizar): ")
        palabra=palabra.lower()
        if palabra!="salir":
            print(f"\nLa palabra {palabra} tiene {contar_vocales(palabra)} vocales.")

def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador
        
def ejercicio_ocho():
    lista_elementos=[1,1,1,2,3,4,4,5,6,7,7,8,9]
    lista_unica = [numero for numero in lista_elementos if lista_elementos.count(numero) == 1]
    print(f"\nLista completa {lista_elementos}")
    print(f"\nLista sin elementos duplicados {lista_unica}")
    
def ejercicio_nueve():
    lista_uno=[1,2,3,4,5,6,7,8,9]
    print(f"\nEsta es la lista uno: {lista_uno}")
    lista_dos=[1,2,3,4,5,6,7,8,9]
    print(f"\nEsta es la lista dos: {lista_dos}")
    lista_nueva=[]
    lista_nueva=[x*y for x,y in zip(lista_uno,lista_dos)]
    print(f"\nEsta es la lista nueva: {lista_nueva}")

def ejercicio_diez():
    lista_original=[1,2,3,4,5,6,7,8,9,10]
    print(f"\nEsta es la lista original: {lista_original}")
    lista_pares=[]
    lista_impares=[elemento for elemento in lista_original if elemento%2!=0]
    print(f"\nEsta es la lista de los impares: {lista_impares}")
    lista_pares=[elemento for elemento in lista_original if elemento%2==0]
    print(f"\nEsta es la lista de los pares: {lista_pares}")

def ejercicio_once():
    diccionario=[{
        'nombre_apellido': 'Juan Pérez',
        'legajo': '001',
        'nota_parcial1': 85,
        'nota_parcial2': 90,
        'nota_final': 91
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
    }]
    lista_nueva=[]
    lista_nueva=[estudiante['nombre_apellido'] for estudiante in diccionario if estudiante['nota_parcial1']>90 or estudiante['nota_parcial2']>90 or estudiante['nota_final']>90]
    print(f"\nEsta es la lista de estudiantes con mas de 90: {lista_nueva}")



opcion=-1
sigue=True
while sigue==True:
    menu()
    opcion=validar_ejercicio()
    if opcion == 1:
        ejercicio_uno()
    elif opcion == 2:
        ejercicio_dos()
    elif opcion==3:
        ejercicio_tres()
    elif opcion==4:
        ejercicio_cuatro()
    elif opcion==5:
        ejercicio_cinco()
    elif opcion==6:
        ejercicio_seis()
    elif opcion==7:
        ejercicio_siete()
    elif opcion==8:
        ejercicio_ocho()
    elif opcion==9:
        ejercicio_nueve()
    elif opcion==10:
        ejercicio_diez()
    elif opcion==11:
        ejercicio_once()
    else:
        sigue=False
print("FIN")