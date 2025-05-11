persona1 = {
    'nombre':"Pepe Domingo",
    'apellido': "perez", 'edad': 14,
    'telefono': 2966,
    'sueldo': 15.000
    }
# print(persona1['nombre'])

# print(persona1['nombre'].split()[-1])

# print(persona1.keys())
# print(persona1.values())
# print(persona1.items())
# print(len(persona1))
key0, value0 = list(persona1.items())[0]
print(key0, value0)