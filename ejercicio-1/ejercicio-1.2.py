frase = input("Dime una frase y calculo cuanto tardarias si tuvieras q decirla: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dijiste {cantidad_de_palabras} palabras, y Dalto tardaria {cantidad_de_palabras*100//2/1.3 /100} segundos en decirlo')
