#creando un array, se puede
lista = ["Max", "Jean", True, 1.70]
#creando una tupla, no se puede modificar
tupla = ("Max", "Jean", True, 1.70)

lista[0] = "Mashito"

#esto no se puede modificar
#tupla[0] = "mashhh"

print(lista[0])

print(tupla[0])

#creando un conjunto (set) (no se puede llamar a los elementos por sus indices, no almacena datos duplicados)

conjunto = {"Jean", "Max", True, 1.70}

conjunto = {"maquina", "asdasd", False, 1.55}

print(conjunto)

#creando un diccionario

diccionario = {
    'nombre': "max",
    'canal': "Mashito",
    'esta_emocionado' : True,
    'altura': 1.70,
    'dato': "122"
}

print(diccionario['altura'] + 2)

