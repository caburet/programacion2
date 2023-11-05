

def ejercicion1(listaNros):
    listaCuadrada = [elem**2 for elem in listaNros]
    return listaCuadrada


def ejercicio2(listaNombres, cadenacaracteres):
    tamanioCadenaCaracteres = len(cadenacaracteres)

    listaNueva = [valor for valor in listaNombres if len(valor>=tamanioCadenaCaracteres) ]
    return listaNueva

def ejercicio3():
    ruta = "/home/cristina/Documentos/programacion2practica/programacion2/TP3/datos.txt"
    arch = open(ruta,"r")
    lista = [valor for valor in listaNombres if len(valor>=tamanioCadenaCaracteres) ]
    lineas = arch.readlines()
    #strip es para sacar los caracteres en blanco de linea
    lista = [linea.strip() for linea in lineas]
    return lista

def ejercicio4(diccionario,letra):
    nuevaLista = [palabra  for palabra  in diccionario if palabra.startswith(letra)] 

    return nuevaLista


def esprimo(nro):
    return true
def ejercicio5(listaNumeros):
    listaPrimos = [nro  for nro  in listaNumeros if esprimo(nro)] 
    return listaPrimos

def ejercicio6(diccionario, nro): #el diccionario tiene nombre y edad
    lista = [nombre  for nombre, edad  in diccionario if edad > nro] 
    return lista

def leerPalabra():
    return"ds1fawbeaaeio"

def ejercicio7():
    palabra = leerPalabra()
    while(palabra!="salir"):
        cantidad = 0
        vocales = [cantidad+1  for letra  in palabra if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'] 
        cantidad = len(vocales)
        print(f"la palabra {palabra} tiene {cantidad} vocales")
        palabra=leerPalabra()


#[] 

ejercicio7();