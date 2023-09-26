# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='11-05-1997'  
minombre='Camila Piergentili'
milegajo=21535
midni=38944251
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 4.
# ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2

def hashFecha(stringfecha):
    dia, mes, anio = stringfecha.split('-')

    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    sumafecha = (dia + mes + anio)
    division = (sumafecha % 4)

    print(division)

    return division

hashFecha(mifecha)
  
# 2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

#El algoritmo de ordenacion burbuja inicia en la posicion 0 y compara con el elemento que tiene a su derecha, si este es 
# menor o mayor (dependiendo como se lo desea ordenar), los intercambia 

def ordenamiento_burbuja(lista):
    tamanio_lista = len(lista)

    for i in range(tamanio_lista - 1):
       for j in range(tamanio_lista -1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


# 3 )  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(archivo):
    ruta = "C:\\Users\\camal\\OneDrive\\Desktop\\Instaladores de apps\\PROGRAMACION II\\MI_programacion2\\PracticaParcial\\datos.csv"
    lista=[]
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            prod1, prod2, prod3 = linea.split(',')
            prod1 = prod1.strip('.,!¡?\n')

            prod1 = str(prod1)
            prod2= float(prod2)
            prod3 = int(prod3)

            lista.append({'nombre': prod1, 'precio': prod2, 'cantidad': prod3})
    print(lista)

    return lista
archivo = "C:\\Users\\camal\\OneDrive\\Desktop\\Instaladores de apps\\PROGRAMACION II\\MI_programacion2\\PracticaParcial\\datos.csv"
crearStock(archivo)

#4) Crear dos funcion que utilizando la estructura del punto 3. Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):

    lista_nueva = sorted(lista, key=lambda x: x["precio"], reverse=True)
    nombre_producto = lista_nueva[0]
    print(f"El nombre del producto más caro es: {nombre_producto}")
   
    return nombre_producto



def productoMenorCantidad(lista):

    lista_menor = sorted(lista, key=lambda x: x["cantidad"])
    nombre_producto_menor = lista_menor[0]
    print(f"El producto de menor cantidad es: {nombre_producto_menor}")

    return nombre_producto_menor



# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(producto):
    suma = 0
    for producto in lista:
        producto['precio'] = float(producto['precio'])
        producto['cantidad'] = int(producto['cantidad'])
        multiplicacion_productos = producto['precio']*producto['cantidad']
        suma+= multiplicacion_productos

    print(suma)
        
    return suma

lista = crearStock(archivo)
productoMasCaro(lista)
productoMenorCantidad(lista)
totalGanancia(lista)
