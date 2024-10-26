# Una tienda ofrece descuentos en las ventas de televisores, un cliente desea 
# comprar un televisor, se necesita calcular el monto de descuento, el cual es el 
# 2% del precio del televisor que desea. 

precio = int(input("Cuanto cuesta la television que quieres comprar? "))
descuento = 0.02

monto_descuento = precio * descuento
monto_descuento = str(monto_descuento)

print("EL monto de descuento es: " + monto_descuento)