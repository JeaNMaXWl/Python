### Exception Handling (manejo de errores) ###
num1, num2 = 5, 1
num2 = "1"
# print( num1 + num2)

# if type(num2) == int:
#     print(num1+num2)
# else:
#     print("No se cumplió")


#try except
try:
    print(num1+num2)
    print("no se ha producido un error")
except:
    #se ejecuta si se produce una excepcion
    print("se ha producido un error")
    
#try except else
try:
    print(num1+num2)
    print("no se ha producido un error")
except:
    print("se ha producido un error")
else: #opcional
    print("La ejecición continúa correctamente")
    
#try except else finally
try:
    print(num1+num2)
    print("no se ha producido un error")
except:
    print("se ha producido un error")
else: #opcional
    print("La ejecición continúa correctamente")
finally: #opcional
    print("La ejecusion continnúa")
    

#Excepciones por tipo
# try:
#     print(num1+num2)
#     print("no se ha producido un error")
# except TypeError:
#     print("se ha producido un error")

try:
    print(num1+num2)
    print("no se ha producido un error")
except ValueError as error:
    print(error)
except Exception as expection:
    print("Exception xd")