#escribir un programa que calcule la serie de fibonacci hasta un numero especifico de terminos

#que es la serie fibonacci
#0,1,1,2,3,5,8

def fibonnacci(num):
    serie = [0, 1]
    count = 0
    for i in range(num):
        base = serie[count] + serie[count + 1]
        count = count + 1
        if base < num:
            serie.append(base)
        else:
            break
    return serie
        
print(fibonnacci(145))
print('lo logre ctm')

def fibonacci(num):
    a,b = 0,1
    lista = [a]
    for i in range(num):
        if b > num : return lista
        else: 
            lista.append(b)
            a,b = b, a+b    
print(fibonacci(145))
print('lo logre ctm')

