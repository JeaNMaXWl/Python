#usando open para abrir un archivo con una cpdificacion universal (UTF-8)
archivo_sin_leer = open ("archivos\\texto_de_Max.txt", encoding = "UTF-8")

#leer archivo completo
archivo = archivo_sin_leer.read()

#leer lineas
# linea_1 = archivo_sin_leer.readlines()
# print(archivo)

#leer una sola linea
# linea_1 = archivo_sin_leer.readline()


#cerrar el archivo con close
archivo.close()
print(archivo.read())

# print(linea_1)


