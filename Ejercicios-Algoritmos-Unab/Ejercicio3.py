#Se necesita convertir un monto de dinero que está en soles a dólares, se sabe que el tipo de cambio es 3.82

monto = int(input("Cual es el mondo a convertir? "))
dolar_a_soles = 3.82 

monto = str(int(monto * dolar_a_soles))

print("EL mondo a doles es: $" + monto)