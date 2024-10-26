#creando un conjunto con set()

conjunto = set(["Dato1"])

#metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,8}

#verificando si es un subconjunto
resultado1 = conjunto2.issubset(conjunto1)
resultado2 = conjunto1.issubset(conjunto2)
resultado3 = conjunto2 <= conjunto1

#verificando si es un subconjunto
resultado1 = conjunto2.issuperset(conjunto1)
resultado2 = conjunto1.issuperset(conjunto2)
resultado3 = conjunto2 > conjunto1

#verificando si algun numero es comun
resultado4 = conjunto2.isdisjoint(conjunto1)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)


#verificando si es un subconjunto
