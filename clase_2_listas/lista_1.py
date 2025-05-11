mi_variable = 1
mi_variable2 = "Pera"

mi_lista = [mi_variable, mi_variable2, 1.2, ""]

# print( mi_lista[2], " --- ", mi_lista[-2])

auto = [ "auto1", "auto2" ]
resultado = mi_lista + auto
# print(resultado)

#________----------_________


"""
los enteros son inmutables
los strings son inmutables
listas mutables
diccionarios mutables
"""


persona1 = ["Pepe Grillo", "Perez", 4, "123456", "300.000"]
persona2 = ["Ñeeeeee", "Perez", 12, "123456", "340.000"]
persona3 = ["Josefa", "Perez", 45, "123456", "60.000"]
personas = [persona1, persona2]
personas.append(persona3)
# print(personas[2] * 2)

empleados = []
empleados.extend([persona1, persona2])
# print(empleados)

print(persona1[0].split()[-1])





