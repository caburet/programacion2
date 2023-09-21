#Implemente una función que dada una lista de nombres, 
#devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual#
# a una cantidad de caracteres pasada por parámetro, 
#utilizando list comprehensions.

def ListaNombres(longitudCadena,name_list):
    new_list=[name for name in name_list if len(name)>=longitud_cadena]
    return new_list

#Declaracion de una lista con diferentes nombres
name_list=["Eros","Matias",'Maria','John','Maximiliano','Cristina']
longitud_cadena=int(input("Ingrese el largo de la cadena"))
new_list=ListaNombres(longitud_cadena,name_list)
print(new_list)