#creando las listas
frutas = ["manzana", "pera", "granada", "platano", "mandarina", "uva"]
cadena = 'Hola Mashito'
numeros = [2,5,8,10]

#evitando que se coma una granada xd
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'Me voy a comer una {fruta}')
print('________________________________')
#evitar que el bucle siga ejecutandose {el else no se ejecuta}
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
else:
    print('buble terminado')

print('_______________________________')

#recorrer una cadena de texto
for letra in cadena:
    print(letra)
else:
    print("________________________________")

#for en una sola linea de codigo
#numeros_duplicados = list()
#for num in numeros:
#    numeros_duplicados.append(num*2)
#else:
#    print(numeros_duplicados)

numeros_duplicados = [x**2 for x in numeros]
print(numeros_duplicados)