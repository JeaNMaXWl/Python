#creando una funcion que devuelva los numeros primos desde el 2 hasta que que pida

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    for i in range(2, num-1):
        if num%i==0:
            return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(num):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos
resultado1, resultado2 = es_primo(25), primos_hasta(25)
print(resultado1)
print(resultado2)