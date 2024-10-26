#Se tiene la medida del largo de una pared expresada en metros, se desea convertir esa cantidad en metros a centimetros

largo = float(input("Largo de la pared: "))
metros_a_centimetros = 100

largo_en_centimetros = largo*metros_a_centimetros
largo_en_centimetros = str(largo_en_centimetros)

print("El largo a centimetros es: " + largo_en_centimetros)
