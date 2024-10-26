#Hugo, Paco y Luis aportan un monto de dinero cada uno para comprar los instrumentos para su banda musical, Hugo y Paco aportan en dólares y Luis en soles. Determina el monto total de dinero acumulado en dólares
hugo_dolar = int(input("Dinero q aporta Hugo: "))
paco_dolar = int(input("Dinero q aporta Paco: "))
luis_soles = float(input("Dinero q aporta Luis: "))
dolar_a_soles = 3.82

monto = str((hugo_dolar + paco_dolar + luis_soles)/dolar_a_soles)

print('El monto total en dólares es: ' + monto)