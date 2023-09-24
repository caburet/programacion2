#11. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente: 

lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]


def Sacar_Prom(lista_dic):
    suma = 0
    cant_alumnos = len(lista_dic)
    for alumnos in lista_dic:
        suma += alumnos['nota']
    promedio = suma / cant_alumnos
    print(suma)
    return promedio

promedio = Sacar_Prom(lista_dic)
print(f"El promedio es de: {promedio}")