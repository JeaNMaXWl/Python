diccionario = {
    "nombre" : 'Max',
    "apellido" : 'Trujillo',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#devuelve el valor de esa parte del diccionario a la variable, no lanza excepcion, si no encuentra el valor continua el programa
claves = diccionario.get("subs")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_item iterable
resultado = diccionario.items()

print(diccionario)
print(claves)
print(resultado)