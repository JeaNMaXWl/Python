### Classes ###

class MyEmptyPerson:#las clases son con CamelCase
    pass

# print(MyEmptyPerson)
# print(MyEmptyPerson())
# print(type(MyEmptyPerson))
# print(type(MyEmptyPerson()))

class Person:
    def __init__(self, name, username, alias = "Sin Alias"):
        self.fullname = f'{name} {username} {alias}'
        self.__name = name #propiedad privada
        self.__username = username #propiedad privada
        
    def get_name (self):
        return self.__name 

    def walk (self):
        print(f'{self.fullname} Está caminando')
    
my_person = Person("Max", "Maxito Wl")
print(my_person.fullname)
print(my_person.get_name())
my_person.walk()
my_other_person = Person("Gisela", "Torres", "GISEE")
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Gissella"
my_other_person.walk()



#para saber como se usa el pass, aqui solo imprime los impares, porque el pass hace que no se perciba el error de que una funcion, clase, bucle o condicional esté vacia.
# for i in range(1,100):
#     if i%2 == 0:
#         pass
#     else:
#         print(i)