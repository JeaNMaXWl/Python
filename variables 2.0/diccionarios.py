#creando diccionarios con dict()
diccionario = dict(nombre = "Max", apellido = "Trujillo")

#las listas no pueden ser claves porq no son mutables
#no pueden ser listas si se usan el frrozen set
diccionario = {frozenset(["max", "treer"]): "XDD"}

#{
#    'nombre' = "Max",
#    'apellido' = "Trujillo"
#}

#creando diccionarios con fromkeys() con dos parametros
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")
#creando diccionarios con fromkeys() cambia el valor por defecto
diccionario = dict.fromkeys("ABSCD", 2)

print(diccionario)