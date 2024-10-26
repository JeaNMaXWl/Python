def saludo(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, es usted {adjetivo}'

print(saludo(adjetivo = "un capo",nombre = "Max", apellido ="Trujillo"))

def frase(nombre, apellido, adjetivo = "tonto"):
    return f'Hola {nombre} {apellido}, es usted {adjetivo}'
print(saludo("Max","Trujillo", "un capo"))