from functools import reduce
mifecha='03-01-2005'  
minombre='Dahua Bruno Martin'
milegajo=21570
midni=45889159
def validar_numeroejercicio():
    menu()
    numero_ejercicio=-1
    while numero_ejercicio<0 or numero_ejercicio>5:
        numero_ejercicio=int(input("Ingrese un numero de ejercicio para ejecutar: "))
        if numero_ejercicio<0 or numero_ejercicio>5:
            print("Vuelva a intentarlo...")
    return numero_ejercicio

def menu():
    print("0) Salir")
    print("\n1) Implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 4.")
    print("ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2")
    print("\n2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.")   
    print("Funcionamiento: Teniendo una lista...")
    print("Algoritmo: ...compara...")
    print("\n3 )  Usando el archivo CSV 'datos.csv' que contiene información sobre productos. El archivo tiene el siguiente formato:")
    print("Nombre, Precio, Cantidad")
    print("Producto1, 10.99, 50")
    print("Producto2, 5.99, 30")
    print("Producto3, 8.49, 75")
    print("Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: 'Nombre' del tipo string, 'Precio' del tipo float")
    print("y 'Cantidad' del tipo entero, y  los valores deben corresponder a los datos del archivo CSV")
    print("\n4) Crear dos funcion que utilizando la estructura del punto 3. Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.")
    print("\n5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)")

def ejercicio_uno():
    fecha_nacimiento=mifecha
    print(f"Esta es la fecha de cumpleaños: {fecha_nacimiento}")
    resto=hashFecha(fecha_nacimiento)
    print(f"La sumatoria del dia, mes y año dividido por 4 da como resto: {resto}")

def hashFecha(stringfecha):
    lista_numeros=[int(numero) for numero in stringfecha.split('-')]
    suma=reduce(lambda x,y:x+y, lista_numeros)
    resultado=suma%4
    return resultado

def ejercicio_dos():
    print("\nFuncionamiento: Teniendo una lista, el metodo de burbuja funciona para ordenarla de acuerdo a como el programador indique (Ej. de mayor a menor o de menor a mayor).")
    print("\nAlgoritmo: Va comparando cada elemento de a pares y los intercambia si estan ordenados de manera incorrecta")
    
def ejercicio_tres():
    diccionario=crear_diccionario()
    print(diccionario)

def crear_diccionario():
    ruta=r"C:\Users\Windows10\Desktop\PracticaParcial\programacion2\PracticaParcial\datos.csv"
    archivo=open(ruta,"r")
    datos={}
    for linea in archivo:
        elemento=linea.split(",")
        nombre=elemento[0]
        precio=float(elemento[1])
        cantidad=int(elemento[2])
        datos[nombre]={"precio":precio,"cantidad":cantidad}
    return datos

def ejercicio_cuatro():
    diccionario=crear_diccionario()
    mas_caro=productoMasCaro()
    menor_cantidad=productoMenorCantidad()
    #menos_cantidad=productoMenorCantidad()
    print(f"\nEl producto mas caro es: {mas_caro}")
    print(f"\nEl producto que menor cantidad hay es: {menor_cantidad}")

def productoMasCaro():
    valor_caro=0
    nombre_caro=""
    diccionario=crear_diccionario()
    for nombre, producto in diccionario.items():
        precio=producto["precio"]
        if precio>valor_caro:
            valor_caro=precio
            nombre_caro=nombre
    return nombre_caro

def productoMenorCantidad():
    cantidad_menor=100
    nombre_menor=""
    diccionario=crear_diccionario()
    for nombre,producto in diccionario.items():
        cantidad=producto["cantidad"]
        if cantidad<cantidad_menor:
            cantidad_menor=cantidad
            nombre_menor=nombre
    return nombre_menor

def ejercicio_cinco():
    ganancia_total=totalGanancia()
    print(f"La ganancia total es de ${ganancia_total}")

def totalGanancia():
    diccionario=crear_diccionario()
    ganancia=0
    cantidad=0
    precio=0
    for nombre, producto in diccionario.items():
        precio=producto["precio"]
        cantidad=producto["cantidad"]
        ganancia+=precio*cantidad
    return ganancia

seguir=True
while seguir==True:
    ejercicio=validar_numeroejercicio()
    if ejercicio==1:
        ejercicio_uno()
    elif ejercicio==2:
        ejercicio_dos()
    elif ejercicio==3:
        ejercicio_tres()
    elif ejercicio==4:
        ejercicio_cuatro()
    elif ejercicio==5:
        ejercicio_cinco()
    else:
        seguir=False
print("Practica de parcial terminada.")