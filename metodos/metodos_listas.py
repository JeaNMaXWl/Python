#Creando una lista con list()
lista = list(["hola","dalto",34])

cadena = "hola"
#Devuelve los elementos de una lista
resultado = len(lista)


#agregando un elemento a la lista
resultado = lista.append(True)

#agrega un elemento a la lista en un indice especifico
resultado = lista.insert(2,"Mamamia")

#agrega al final varios elementos a la lista
resultado = lista.extend(["Jean", "Max"])

#eliminando un elemento de la lista por su indice
lista.pop(0)

#elimina el ultimo elemento
lista.pop(-1)

#removiendo un elmento de la lista por su valor
lista.remove("Jean")

#eliminando todos los elementos de la lista
lista.clear()

lista.extend([6,5,2,4,3,True, False, True,1])

#para ordenar cuando no hay cadenas de texto
lista.sort() #los False van primero, luego los True, y luego los numeros ordenados de menor a mayor

lista.sort(reverse=True) #Esto es para que lo ordenen al revez, osea de mayor a menor

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
resultado = lista.index(2)

print(resultado)
print(lista)

#conjunto = set(["Jean", "Max"]).index("max")     ---> no se puede usar index en un set(conjuntos)

print(dir(set(["Hola", "Mash"])))