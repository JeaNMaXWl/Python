#falto el profe y los chicos van a armar una clase

#pedir el nombre y la edad de los compañeros que vinieron a clase
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(7):
        nombre = input("ingrese el bombre del compañero")
        edad = int(input("ingrese la edad del compañero"))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor
asistente, profesor = obtener_compañeros(5)
print(f'El profesor es: {profesor} y su asistente es {asistente}')