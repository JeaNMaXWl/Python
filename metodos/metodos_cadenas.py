cadena1 = "hola,Mashito,cojudo"
cadena2 = "Hello capo"

#primera letra en mayuscula
resultado = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
resultado = cadena1.find("M")

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
resultado = cadena1.index("o")

#si es numerico, devolvemos true, si no devuelve falso
resultado = cadena1.isnumeric()

#Si es alfanumerico devilvemos true, sino devolvemos false
resultado = cadena1.isalpha()

#Contamos coincidencias de una cadena dentro de otra cadena, Devuelve cuantas veces encuentra una coincidencia
resultado = cadena1.count("o")

#Cuenta la cantidad de caracteres en una cadena
resultado = len(cadena1)

#verificamos si uuna cadena empieza con otra cadena, si es asi devuelve true
resultado = cadena1.startswith("Hoo")

#verificamos si uuna cadena termina con otra cadena, si es asi devuelve true
resultado = cadena1.endswith("a")

#reemplaza un pedazo de la cadena dada por otra dada
resultado = cadena1.replace("Ho", "Jean")
resultado = cadena1.replace("holaaa", "Jean")

#separar cadenas con la cadena que le pasemos
resultado = cadena1.split(",")


print(type(resultado))
print(resultado)
print(resultado[0])
