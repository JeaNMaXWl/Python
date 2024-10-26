#si el modulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

import sys
sys.path.append("C:\Max\Programacion\Python\\funciones_buenas")
print(sys.path)

import saludar as m_saludar

print(m_saludar.saludar("Max"))