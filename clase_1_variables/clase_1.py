mi_variable = 3
print(mi_variable)

mi_variable = "hola "
print(mi_variable)

""" 
    Comentario de varias lineas
"""

# Variables comentario de una linea 


#✅ Ejemplos simples de asignación dinámica

x = 5         # x es un entero
print(type(x))  # <class 'int'>

x = "hola"    # ahora x es un string
print(type(x))  # <class 'str'>

x = [1, 2, 3]  # ahora x es una lista
print(type(x))  # <class 'list'>


#  ¿Por qué se dice "dinámica"?
#  Porque el tipo se decide en tiempo de ejecución y podés cambiarlo libremente:

def asignar_valor(valor):
    variable = valor
    return variable

print(asignar_valor("ponemos un primer valor")) 
print(asignar_valor("segundo valor que queramos"))
