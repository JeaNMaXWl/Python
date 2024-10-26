animales = ["perro", "gato", "loro", "delfin"]
numeros = [10,62,12,72]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a {animal}')

#recorriendo la lista numeros y multiplicandolo por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas en el mismo tamaño al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

for num in range(5,10):
    print(num)

for num in range(10):
    print(num)

#forma no optima de recorrer una lista con su indice 
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
    #enumarate itera dando tuplas
    print(num)
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando el else
for num in numeros: 
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
else:
    print("El bucle terminó")

for num in animales: 
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
else:
    print("El bucle terminó")

#todo lo anterior funciona exactamente igual para tuplas, listas y diccionarios