#Implementa una función hashFecha2(stringfecha) que tome una cadena de fecha en el formato "dd-mm-yyyy" y devuelva un valor hash basado en la suma de los números de
# día, mes y año siguiendo estas reglas:

#Si el año es par, suma los números de día y mes, luego eleva el resultado al cuadrado y devuelve el residuo de la división por 5.
#Si el año es impar, suma los números de día y mes, luego eleva el resultado a la tercera potencia y devuelve el residuo de la división por 5.
#Si la suma de día y mes es un número primo, suma el año al resultado anterior y devuelve el residuo de la división por 6.
#Si la suma de día y mes no es un número primo, resta el año al resultado anterior y devuelve el residuo de la división por 7.

#Asegúrate de incluir manejo de errores para verificar que la cadena de fecha esté en el formato correcto y que los valores de día, mes y año sean números enteros.

def hashFecha2(stringfecha):
    return 0

#2) ¿Qué es un "Pull Request" (PR) en GitHub y cuál es su propósito en un proyecto colaborativo?

#3) Dada la siguiente lista ordenar alfabeticamente los nombres sin distingir entre mayuscula y minusculas.
nombres = ["Alice", "Bob", "Charlie", "david", "Ella", "Frank", "Grace", "harry", "Isabel", "Jack", "Karen", "Liam", "Mia", "Noah", "Olivia", "peter", "Quinn", "Rachel", "Sarah", "Tom", "Ursula", "Victor", "Wendy", "Xander", "Yasmine", "Zane"]
def ordenarNombres(listanombres):
    return  listanombres

#4) Se organizo una venta de tallarines en el club para recaudar fondos. Cada paquete de tallarines se vendio a $50 y se compraron un total de 100 paquetes.
# Se cargo en un archivo CSV la siguiente informacion:
# Nombre Comprador, Cantidad de paquetes
# Procese la información y confirme las ventas hasta donde alcance. 
# Ejemplo: Hay 10 paquetes. 
# 1° en el archivo compro 5. 
# 2° compro 3. 
# 3° quiso comprar 15 pero solo quedaban 2.
# 4° no pudo comprar porque no habia mas.
# Imprimir por pantalla la información de las ventas realizadas indicando nombre comprador y cantidad de paquetes y quienes se quedaron sin poder comprar.
# ruta archivo para usar F5: PrimerParcial\compradores.csv
def procesarVentas(rutaArchivoCSV,cantidadPaquetesDisponibles):
    return None

#5) Implementar una función que reciba un diccionario con las claves como nombres de personas y los valores como edades y devuelva un diccionario con las claves como edades y los valores una LISTA con los nombres de las personas de esa edad.
dicEdades = {"Juan":30,"María":25,"Carlos":35,"Ana":28,"Luis":32,"Laura":29,"Pedro":31,"Sofía":26,"Miguel":27,"Isabel":24,"Diego":33,"Valentina":22,"Javier":29,"Carmen":40,"Andrés":38,"Lucía":27,"Ricardo":36,"Victoria":23,"Gabriel":34,"Fernanda":31,"Max":29,"Diana":28,"Rodrigo":30,"Camila":25,"Gonzalo":33,"Daniela":27,"Emilio":29,"Marcela":34,"José":39,"Valeria":26,"Andrea":30,"Raúl":42,"Sara":24,"Rafael":36,"Elena":25,"Martín":32,"Beatriz":28,"Pablo":37,"Lorena":30,"Ángel":29,"Paula":26,"Luisa":35,"Arturo":31,"Mónica":27,"Manuel":28,"Verónica":29,"Carlos":40}
# Resultado esperado
#personas_por_edad = {
#    22: ["Valentina"],
#    23: ["Victoria"],
#    24: ["Isabel", "Sara"],
#    25: ["María", "Laura", "Elena", "Camila"],
def invertirDiccionario(diccionario):
    diccionarioinvertido = {}
    return diccionarioinvertido

