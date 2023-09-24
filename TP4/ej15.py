#Filtrar una lista de diccionarios por una condición. Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.

lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

def AlumnosAprobados(lista_dic):
    list_aprobados = list(filter(lambda x:x['nota'] >= 70,lista_dic))
    return list_aprobados

aprobados = AlumnosAprobados(lista_dic)
print(aprobados)