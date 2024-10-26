#encontrando el numero mayor de una lista
numeros = [1,4,5,87,665,120]

numero_mas_alto = max(numeros)
numero_mas_chico = min(numeros)

print(numero_mas_alto)
print(numero_mas_chico)

#redondeando a 6 decimales

num = 55.245587566
numero_redondeado = round(num, 6)
print(numero_redondeado)

#retorna false ---> 0, vacio, false, ninguno
resultado_bool1 = bool("13.5")
print(resultado_bool1)

#retorna True, si todos los valores son verdaderos
resultado_all = all([True, "True", 0])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)

