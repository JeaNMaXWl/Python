#Calcular el pago final por alquilar una casa sabiendo que son S/30.00 por cada habitacion mas S/10.00 por cada baño y S/15.00 por cada patio.
#DATOS
num_baño = int(input("cuantas habitaciones tiene esa casa "))
num_habitacion = int(input("cuantos baños tiene "))
num_patio = int(input("cuantos patios tiene "))
precio_habitacion = 30.00
precio_baño = 10.00
precio_patio = 15.00

#PROCEDIMIENTO
pago_final = str(num_habitacion*precio_habitacion + num_baño*precio_baño + num_patio*precio_patio)

#SALIDA
print('El pago final es: S/' + pago_final)