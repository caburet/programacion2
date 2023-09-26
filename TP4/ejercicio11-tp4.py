# 11. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso.
# Puede usar una lista como la siguiente: 

# lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, 
#{'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

def main():
    lista_dic = [
        {'nombre': 'Hector', 'nota': 70},
        {'nombre': 'Juan', 'nota': 45},
        {'nombre': 'Maria', 'nota': 75},
        {'nombre': 'Pedro', 'nota': 80},
        {'nombre': 'Ana', 'nota': 60},
        {'nombre': 'Florencia', 'nota': 95}
    ]

    acumulador = 0

    for linea in lista_dic:
        acumulador+= linea["nota"]

    promedio = acumulador/6
    
    print(f"El promedio total del curso es de {promedio}")

main()