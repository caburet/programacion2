#. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.

first_dict = {
    "Crisalida": "Pupa de insecto",
    "Efímero": "De corta duracion",
    "Sandia": "fruta de color verde",
    "Quimera": "Imaginación extravagante",
    "Voraz": "Come con avidez",
    "Crisalidaee": "Pupa de insecto",
    "Efímerodas": "De corta duracion",
    "Sandiawq": "fruta de color verde",
    "Quimeradc": "Imaginación extravagante",
    "Vorazqwq": "Come con avidez",
}
new_list = []
letra_ind = input("Ingrese la letra con la que desee que empiece: ").upper()
new_list = [word for word in first_dict.keys() if word.startswith(letra_ind) ]

print(new_list)