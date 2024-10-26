# with open('archivos\\texto_de_Max.txt', 'w',encoding="UTF-8") as archivo:
#     #sobreescribiendo el archivo
#     # archivo.write("Jajaj, pendejo")

#     #acumula escribiendo en el archivo
#     archivo.writelines(["Hola maestro\n", "Misericordia\n"])
#     archivo.writelines(["Hola maestro\n", "Misericordia\n"])
#     archivo.writelines(["Hola maestro\n", "Misericordia\n"])

with open('archivos\\texto_de_Max.txt', 'a',encoding="UTF-8") as archivo:
    # archivo.write("Jajaj, pendejo")
    # archivo.write("Jajaj, pendejo")
    # archivo.write("Jajaj, pendejo")
    # archivo.write("Jajaj, pendejo")

    for i in range(1,5):
        archivo.write(f'\nLinea {i}\n')
