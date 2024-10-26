edad = 17
usuario_de_base_de_datos = "Max"
usuario_escrito = "Max"

if (usuario_escrito == usuario_de_base_de_datos):
    print("Puedes pasar")
    print("forma parte del if")
else:
    print("No puedes pasar")
    print("forma parte del else")
print("No forma parte de ninguna condicion")

ingreso_mensual = 6000

if ingreso_mensual>10000:
    if gasto_mensual < 7000:
        print("ahora si estas bien")
    else:
        print("Estas bien en cualquier parte del mundo")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en Argentina")
else:
    print("eres pobre xd")