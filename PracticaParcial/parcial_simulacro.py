from functools import reduce

mifecha = "21-01-2004"
minombre = "Pedro Weyland"
milegajo = 21899
midni = 45501926

# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero
#    del año y devuelva el resto de dividirlo por 4. ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2


def validar_num(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("Error, al pasar a entero, verifique el valor ingresado")

def hashFecha(stringfecha):
    fecha_valida = []
    
    #Separo por cada elemento de la fecha en una lista
    fecha_lista = stringfecha.split("-")
    #Valido que sean numeros
    fecha_valida.append(validar_num(fecha_lista[0]))
    fecha_valida.append(validar_num(fecha_lista[1]))
    fecha_valida.append(validar_num(fecha_lista[2]))

    
    suma = fecha_valida[0] + fecha_valida[1] + fecha_valida[2]

    return suma % 4


#print(f"El resultado es: {hashFecha(mifecha)}")

# 2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

# El algoritmo burbuja funciona mediante la comparacion de dos elementos, adyacentes en una lista,
# esto mediante una iteracion de dos 'for', luego de esto entra un 'if' para que compare dichos elementos
# y dependiendo la comparacion mueve los elementos de lugar para ordenarlos de menor a mayor. 
# (no neceseriamente tiene que ser de menor a mayor)


# 3 )  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(ruta):
    lista=[]

    #Abro el archivo CSV
    archivo = open(ruta)
    
    #Leo linea por linea el archivo

    for linea in archivo:
        #Separo la linea en elementos por la coma
        aux = linea.split(",")

        #Agrego a un diccionario los elementos separados
        diccionario = {"Nombre" : aux[0], "Precio": float(aux[1]), "Cantidad": int(aux[2])}
        
        #y agrego el diccionario a la lista
        lista.append(diccionario)

    archivo.close()

    return lista

lista = crearStock("datos.csv")

#print(lista)


#4) Crear dos funcion que utilizando la estructura del punto 3.  
#   Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.

def productoMasCaro(lista):
    max_precio = 0
    
    for i in range(0, len(lista)):
        #Recorro la lista y el diccionario con el key 'Precio'
        if lista[i]["Precio"] > max_precio:
            #Voy guardando el precio mas alto encontrado en 'max_precio'
            max_precio = lista[i]["Precio"]        
            
            #Guardo en una lista aparte la informacion del producto
            producto = lista[i]

    
    return producto


def productoMenorCantidad(lista):
    stock = 0
    
    #Busco el producto con mayor cantidad
    
    for i in range(0, len(lista)):
        if lista[i]["Cantidad"] > stock:
            stock = lista[i]["Cantidad"] 
            
    
    #Apartir de tener el producot con mayor cantidad busco el que tiene menos
    
    for i in range(0, len(lista)):
        #Recorro la lista y el diccionario con el key 'Cantidad'
        if lista[i]["Cantidad"] < stock:
            #Voy guardando el stock mas bajo
            stock = lista[i]["Cantidad"] 
                       
            #Guardo en una lista aparte la informacion del producto
            producto = lista[i]

    return producto

#PRODUCTO CARO:

#producto_caro = productoMasCaro(lista)

#nombre_producto = producto_caro["Nombre"]
#precio_producto = producto_caro["Precio"]

#print(f"El producto {nombre_producto} es el mas caro de todos, con un total de ${precio_producto}")

#PRODUCTO DE POCA CANTIDAD 

#producto_escazo = productoMenorCantidad(lista)

#nombre_producto = producto_escazo["Nombre"]
#cantidad_producto = producto_escazo["Cantidad"]

#print(f"El producto {nombre_producto} es el mas escazo, con un total de {cantidad_producto} unidades")


def productoMasCaro_v2(lista):

    #Ordeno la lista mediante el precio de menor a mayor
    lista_ordenada = sorted(lista, key=lambda x: x["Precio"])    
    
    #Retorno el ultimo elemento ya que se que es es el mas caro, (con la key "Nombre")
    return lista_ordenada[-1]["Nombre"]

#mas_caro = productoMasCaro_v2(lista)

#print(mas_caro)

def productoMenorCantidad_v2(lista):

    lista_ordenada = sorted(lista, key=lambda x: x["Cantidad"])

    return lista_ordenada[0]["Nombre"]

menor_cantidad = productoMenorCantidad_v2(lista)

print(menor_cantidad)

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. 
#    Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)

def totalGanancia(lista):

    #Se puede usar reduce de esta forma:
    #La variable 'x' cumple la funcion de acumular lo que va sumando de la multiplicaicon que hay,
    #esta multiplicacion es con la variable 'y' ya que le pongo la 'key' y esto hace que se multiplique el precio por la cantidad,
    #esto itera todo el tiempo hasta que se termine la lista, y de ahi el valor que queda en 'x' es "copiado" a la variable ganancia
    # (El tercer argumento '0,0' es para que 'x' empieze en ese numero)
     
    ganancia = reduce(lambda x, y: x + (y["Precio"] * y["Cantidad"]), lista, 0.0)
    
    print(f"La ganancia posible seria de: {ganancia}")
    return 0

totalGanancia(lista)