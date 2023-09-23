# Importamos la libreria csv
import csv
# Importamos la libreria os.path 
import os.path
# Importamos solo la función reduce del módulo functools
from functools import reduce

# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha='00-00-0000'  
minombre=''
milegajo=21000
midni=30000000
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 4.
# ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2

# Se definio la función hashFecha(stringfecha)
def hashFecha(stringfecha):
  # Asumiendo que el formato de la fecha es dd/mm/aaaa
  dia, mes, año = map(int, stringfecha.split("/"))

  # Sumamos el dia, el mes y el año
  suma = dia + mes + año

  # Hacemos el resto de la suma divido por 4
  resto = suma % 4

  # Retornamos el resto
  return resto

# Probamos la función con algunas fechas
print(hashFecha("22/09/2023")) # Imprime 2
print(hashFecha("01/01/2021")) # Imprime 3
print(hashFecha("31/12/2022")) # Imprime 1

# 2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.
# Funcionamiento: Teniendo una lista...
# El funcionamiento del algoritmo del ordenamiento burbuja es: 
# El algoritmo de ordenamiento burbuja compara y cambia los elementos de una lista hasta que estén en orden.
# Los elementos más pequeños suben y los más grandes bajan, como burbujas.
# El algoritmo termina cuando no hay más cambios.

# Algoritmo: ...compara...
# Primero se crea la lista en donde el usuario puede ingresar lods datos o que ya tenga los datos predeterminados, luego le pasaremos por parametro la lista a la funcion que llamaremos y que vamos crear, definimos la funcion del ordennamiento burbuja con la lista pasada por paremetro, luego le asignamos a una varible n la longitud de la lista usando la funcion len(), vamos a usar dos for, el primero for i in range(n-1) que va a recorrer cada elemento de la lista hasta n-1 y el segundo for j in range(n-1-i) que va a recorrer desde cada elemnto de la lista hasta n-1-i, dentro del segundo for ponemos un if en el que decimos lista[j] > lista[j + 1], osea que si el elemento en la posicion j es mayor al elemnto en la posicion j + 1, le vamos a decir que los inftercambie haciendo lista[j], lista[j + 1] = lista[j + 1], lista[j]

# 3 )  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

#Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float 
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV

# Funcion que lee el archivo
def crearstock(lista_productos):
    # Creamos la ruta
    ruta = "C:/Users/matia/OneDrive/Escritorio/Programacion II TUP/programacion2-2/PracticaParcial/datos.csv"

    # Usamos un bloque try-except para intentar abrir el archivo datos.csv en modo lectura
    try:
        with open(ruta, "r") as archivo:
            # Creamos un objeto lector que nos permite iterar sobre las filas del archivo
            lector = csv.reader(archivo)

            # Recorremos el resto de las filas
            for fila in lector:
                # Creamos un diccionario con los datos de cada fila
                producto = {"Nombre": fila[0], "Precio": float(fila[1]), "Cantidad": int(fila[2])}

                # Añadimos el diccionario a la lista
                lista_productos.append(producto)

            return lista_productos
    except FileNotFoundError:
        # Si el archivo no existe, mostramos un mensaje de error
        print("El archivo datos.csv no existe.")

# Creamos la lista
lista_productos = list()

# Llamamos a la funcion crearstock
lista_productos = crearstock(lista_productos)

# Mostarmos la lista de productos
print(lista_productos)

#4) Crear dos funcion que utilizando la estructura del punto 3. Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
# Función que devuelve el producto más caro de una lista de productos
def producto_mas_caro(lista_productos):
    # Usamos la función max para obtener el producto con el mayor precio

    # El argumento key nos permite especificar que queremos comparar los precios de los productos
    producto = max(lista_productos, key=lambda p: p["Precio"])

    # Devolvemos el producto
    return producto

# Función que devuelve el producto con menor cantidad de una lista de productos
def producto_menor_cantidad(lista_productos):
    # Usamos la función max para obtener el producto con la menor cantidad

    # El argumento key nos permite especificar que queremos comparar las cantidades de los productos

    # Usamos un signo negativo para invertir el orden de la comparación
    producto = max(lista_productos, key=lambda p: -p["Cantidad"])
    # Devolvemos el producto
    return producto

# Creamos dos variables una para pdo
productomascaro = producto_mas_caro(lista_productos)
productomenorcantidad = producto_menor_cantidad(lista_productos)

# Mostramos los productos mas caros y los de menor cantidad
print(f"El productos mas caro es: {productomascaro}")
print(f"El producto con menor cantidad es: {productomenorcantidad}")

# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)

# Definimos una función auxiliar que toma un acumulador y un producto
def ganancia(acumulador, producto):
    # Devolvemos el acumulador más el producto de la cantidad y el precio del producto
    return acumulador + producto["Cantidad"] * producto["Precio"]

# Definimos una función que nos devuelva el total de la posible ganancia
def totalGanancia(lista_productos):
    # Usamos la función reduce para aplicar la función ganancia a los elementos de la lista
    # Inicializamos el acumulador con cero
    return reduce(ganancia, lista_productos, 0)

# Imprimimos el nombre de cada producto y su ganancia individual
for producto in lista_productos:
    print(f"El producto {producto['Nombre']} tiene una ganancia de {ganancia(0, producto)}")

# Imprimimos el total de la ganancia de todos los productos
print(f"El total de la ganancia es {totalGanancia(lista_productos)}")