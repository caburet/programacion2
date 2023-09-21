 #Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.

list=[2,4,2,76,54,76,'Hola','Hola','img']
#Con un condicional y la funcion count(), solamente agrego a la nueva lista los elementos unicos
new_list=[valor for valor in list if list.count(valor)==1]
