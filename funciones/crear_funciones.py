#creando una funcion simple
#def saludar():
#    print("Hola")
#ejecutando la funcion simple
#saludar()

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "maquina"
    else:
        adjetivo = "mi amor"
    print(f'Hola {nombre} como estas {adjetivo}?')
saludar("Max", "Mujer")
saludar("Jean", "hoMbre")
saludar("Jean Max", "Nose")

#crear una funcion que nos retorne multiples valores
def contraseña_random(num):
    chars = "absdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return (contraseña,num)
password, primer_numero = contraseña_random(398)
print(contraseña_random(398))