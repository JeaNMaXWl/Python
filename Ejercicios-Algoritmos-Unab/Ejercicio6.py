# Un empleado tiene su sueldo fijo, y va a recibir un aumento del 20% de su sueldo, se necesita saber cuánto de dinero representa ese 20%. 

sueldo = float(input("Cuanto es tu sueldo? "))
aumento_porcentaje = 0.2

aumento_dinero = sueldo * aumento_porcentaje
aumento_dinero = str(aumento_dinero)

print("El aumento es: " + aumento_dinero)
