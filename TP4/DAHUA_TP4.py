def menu():
    print("\n0. Salir.")
    print("\n1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado.")
    print("\n2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.")
    print("\n3. Crea una función lambda que devuelva el mayor de dos números.")
    print("\n4. A partir de una lista de números existente, cree una nueva lista incrementando en un 15% los valores originales usando map.")
    print("\n5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista:")
    print("personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]")
    print("\n6. Dada una lista con números, filtra los números pares y devolverlos en una nueva lista.")
    print("\n7. Dada una lista de temperaturas en grados centígrados generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es °F=(°C*(9/5))+32.")
    print("\n8. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.")
    print("\n9. Dada una lista de palabras, genera una lista con las iniciales de cada palabra.")
    print("\n10. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente:")
    print("lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]")
    print("\n11. Encuentra el número mayor de una lista utilizando reduce.")
    print("\n12. Utilice reducir para concatenar una lista de cadenas en una sola cadena.")
    print("\n13. Filtrar una lista de diccionarios por una condición. Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.")
    print("\n14. Dada una lista de diccionarios con nombre, fecha de nacimiento, y teléfono, crear una nueva lista con los diccionarios de las personas que aún no cumplieron años respecto a la fecha actual del sistema, y ​​esa lista ordenarla por la fecha de nacimiento de menor a alcalde. Puede usar una lista como la siguiente:")
    print("import datetime")
    print("lista_alumnos = [{'nombre':'Joaquin', 'fecha_nacimiento':datetime.date(1990, 7, 2), 'telefono':'123456789'}, { 'nombre':'Maria', 'fecha_nacimiento':datetime.date(1995, 5, 16), 'telefono':'123456789'}, { nombre':'Pedro', 'fecha_nacimiento':datetime.date(1992, 9, 12), 'telefono':'123456789'}, { 'nombre':'Ana', 'fecha_nacimiento':datetime.date(1991, 9, 22), 'telefono':'123456789'}, { 'nombre':'Florencia', 'fecha_nacimiento':datetime.date(1994, 12, 8), 'telefono':'123456789'}, { 'nombre':'Hector'', 'fecha_nacimiento':datetime.date(1993, 4, 4), 'telefono':'123456789'}]")

def validar_numero():
    numero=-1
    while numero<0 or numero>14:
        numero=int(input("Ingrese numero de ejercicio: "))
        if numero<0 or numero>14:
            print("Vuelva a intentarlo...")
    return numero

def ejercicio_uno():
    x=int(input("Ingrese numero para devolver el cuadrado: "))
    cuadrado=lambda x:x**2
    print(f"El cuadrado de {x} es {cuadrado(x)}")

def ejercicio_dos():
    x=int(input("Ingrese un numero: "))
    y=int(input("Ingrese un numero: "))
    suma=lambda x,y:x+y
    resultado=suma(x,y)
    print(f"{x} + {y} = {resultado}")

def ejercicio_tres():
    x=int(input("Ingrese un numero: "))
    y=int(input("Ingrese un numero: "))
    mayor=lambda x,y: x if x>y else y
    resultado=mayor(x,y)
    print(f"El numero mayor es {resultado}")

def ejercicio_cuatro():
    lista_original=[1,2,3,4,5,6,7,8,9,10]
    incrementar_quince=lambda x: (15*x/100)+x
    lista_nueva=list(map(incrementar_quince,lista_original))
    print(f"Esta es la lista original: \n{lista_original}")
    print(f"Esta es la lista con 15% incrementado: {lista_nueva}")

def ejercicio_cinco():
    personas = [{'nombre': 'Hector', 'edad': 27}, 
                {'nombre': 'Juan', 'edad': 18}, 
                {'nombre': 'Maria', 'edad': 32}, 
                {'nombre': 'Pedro', 'edad': 21}, 
                {'nombre': 'Ana', 'edad': 20}]
    personas_ordenadas=sorted(personas, key=lambda x:x['edad'])
    print(personas_ordenadas)

def ejrcicio_seis():
    lista_original=[1,2,3,4,5,6,7,8,9,10]
    lista_pares=list(filter(lambda x:x%2==0, lista_original))
    lista_impares=list(filter(lambda x:x%2!=0, lista_original))
    print(f"Esta es la lista original: {lista_original}")
    print(f"Esta es la lista de numeros pares: {lista_pares}")
    print(f"Esta es la lista de los impares: {lista_impares}")

def ejercicio_siete():
    lista_centigrados=[1,2,3,4,5,6,7,8,9,10]
    lista_fahrenheit=[elemento*(9/5)+32 for elemento in lista_centigrados]
    print(f"Esta es la lista de temperaturas en grados: {lista_centigrados}")
    print(f"Esta es la lista de temperaturas en fahrenheit: {lista_fahrenheit}")

def ejercicio_ocho():
    lista_original=['cuatro','cinco','ocho','tres','dos','si','u']
    lista_ordenada = sorted(lista_original, key=lambda palabra: len(palabra))
    print(f"Esta es la lista de palabras: {lista_ordenada}")
    print(f"Esta es la lista de palabras ordenadas: {lista_ordenada}")

def ejrcicio_nueve():
    lista_original=['Hola','soy','Bruno','Martin','Dahua']
    lista_nueva=[palabra[0] for palabra in lista_original]
    print(f"Esta es la lista de palabras: {lista_original}")
    print(f"Esta es la lista de iniciales: {lista_nueva}")

from functools import reduce
def ejercicio_diez():
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
    suma_notas=0
    cantidad_notas=len(lista_dic)
    print(f"La cantidad de notas: {cantidad_notas}")
    for estudiantes in lista_dic:
        suma_notas=suma_notas+estudiantes['nota']
    promedio=suma_notas/cantidad_notas
    print(f"Este es el promedio de notas: {promedio}")

def ejercicio_once():
    lista_original=[10,9,8,7,6,5,4,3,2,1]
    menor=reduce(encontrar_menor,lista_original)
    print(f"El numero menor es {menor}")

def encontrar_menor(x,y):
    if x<y:
        return x
    else:
        return y

def ejercicio_doce():
    lista_original=["Hola ","mi ","nombre ","es ","Bruno","."]
    texto=reduce(concatenar,lista_original)
    print(f"Estas son las cadenas concatenadas: {texto}")

def concatenar(cadena1,cadena2):
    return cadena1+cadena2

def ejercicio_trece():
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
    nota_aprobacion=60
    lista_aprobados=[nota['nombre'] for nota in lista_dic if nota['nota']>=60]
    print(f"Esta es la lista de aprobados: {lista_aprobados}")


def ejercicio_catorce():
    import datetime
    fecha_actual = datetime.date.today()
    lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]
    print(f"Esta es la lista de alumnos: {lista_alumnos}")
    personas_sin_cumpleanos = [alumno for alumno in lista_alumnos if (alumno["fecha_nacimiento"].month, alumno["fecha_nacimiento"].day) > (fecha_actual.month, fecha_actual.day)]
    personas_sin_cumpleanos.sort(key=lambda x: x["fecha_nacimiento"])
    for alumno in personas_sin_cumpleanos:
        print(f"Nombre: {alumno['nombre']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Teléfono: {alumno['telefono']}")

sigue=True
while sigue==True:
    menu()
    numero_ejercicio=validar_numero()
    if numero_ejercicio==1:
        ejercicio_uno()
    elif numero_ejercicio==2:
        ejercicio_dos()
    elif numero_ejercicio==3:
        ejercicio_tres()
    elif numero_ejercicio==4:
        ejercicio_cuatro()
    elif numero_ejercicio==5:
        ejercicio_cinco()
    elif numero_ejercicio==6:
        ejrcicio_seis()
    elif numero_ejercicio==7:
        ejercicio_siete()
    elif numero_ejercicio==8:
        ejercicio_ocho()
    elif numero_ejercicio==9:
        ejrcicio_nueve()
    elif numero_ejercicio==10:
        ejercicio_diez()
    elif numero_ejercicio==11:
        ejercicio_once()
    elif numero_ejercicio==12:
        ejercicio_doce()
    elif numero_ejercicio==13:
        ejercicio_trece()
    elif numero_ejercicio==14:
        ejercicio_catorce()
    else:
        sigue=False
print("Gracias")


print("FIN")



