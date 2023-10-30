from functools import reduce
# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='00-00-0000'  
minombre=''
milegajo=21000
midni=30000000
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 4.
# ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2

def hashFecha(stringfecha):
    separarlo= stringfecha.split('-')
    if (len(separarlo)==3):
        try:
            dia = int(separarlo[0])
            mes = int(separarlo[1])
            anio = int(separarlo[2])
        except ValueError:
            return False
        total= dia + mes +anio

    return total % 4

# 2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.    
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

# 3 )  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

def crearStock(rutaarchivo):
    stock = []  
    with open(rutaarchivo, mode='r') as file:
        lines= file.readlines()
        for line in lines:
            nombre, precio, cantidad = line.split(',')
            producto = {
                "Nombre": nombre,
                "Precio": float(precio),
                "Cantidad": int(cantidad)
            }
            stock.append(producto)
    return stock

#4) Crear dos funcion que utilizando la estructura del punto 3. Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    precio_mas_alto = 0
    nombre_producto_mas_caro=''
    for producto in lista:
        if producto["Precio"] > precio_mas_alto:
            nombre_producto_mas_caro = producto["Nombre"]
    return nombre_producto_mas_caro

def productoMenorCantidad(lista):
    Menor_cantidad = 100
    nombre_menor_cantidad=''
    for producto in lista:
        if producto["cantidad"] < Menor_cantidad:
            Menor_cantidad = producto["cantidad"]
            nombre_menor_cantidad = producto["Nombre"]
    return nombre_menor_cantidad

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    return reduce(lambda x, producto: x + float(producto['precio']) * int(producto['cantidad']), lista, 0.0)