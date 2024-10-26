#forma no optima de sumar una lista
# def suma(lista):
#     suma = 0
#     for numero in lista:
#         suma = suma + numero
#     return suma

# resultado = suma([5,3,4,3,5,4,6])
# print(resultado)
#utilizando el parametro args
def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es {sum(numeros)}'


resultado = suma("Max",4,5,6,4)
print(resultado)

def suma_total(numeros):
    return sum([*numeros])
resultado = suma_total([4,5,6,4])
print(resultado)