diccionario = {
    "nombre": "Max",
    "apellido": "Trujillo",
    "subs": 1000000
}

for key in diccionario.items():
    print(key)

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el valor es: {value}')
