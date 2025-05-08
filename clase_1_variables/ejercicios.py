# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

#Ejercicio N°1 -> Ejercicio 1:
"""Cree un programa que tome tres valores por consola multiplique el primero por el segundo y le sume el tercero. Presente el resultado en la terminal."""

variable1 = 2
variable2 = 5
variable3 = 3

print(variable1 * variable2 + variable3)

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------


#Ejercicio N°2 -> Ejercicio 2:
"""Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si son múltiplos de dos"""


nombre = "Daniel"
print(f"Hola, {nombre}! Este es el ejercicio 2")  # ➜ Hola, Daniel! Permite insertar variables directamente dentro del texto, usando llaves {}.




# python ejercicios.py 2 4 6

import sys

if len(sys.argv) != 4:
    print("tenes que ingresar 3 numeros")
    print("ejemplo: python ejercicio.py 2 4 6")
    sys.exit(1)

#recibir valores enteros

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = int(sys.argv[3])

#verificar si son multiplos de 2
if n1 % 2 == 0:
    print(f"{n1} es multiplo de 2")
else:
    print(f"{n1} no es multiplo de 2")
if n2 % 2 == 0:
    print(f"{n2} es multiplo de 2")
else:
    print(f"{n2} no es multiplo de 2")
if n3 % 2 == 0:
    print(f"{n3} es multiplo de 2")
else:
    print(f"{n3} no es multiplo de 2")


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

#Ejercicio N°3 -> Ejercicio 3:

"""Ejercicio 3:
Escriba un programa que solicite el
perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio 
"""

radio = (float(input("Ingrese el radio: ")))

pi = 3.1416

longitud = 2 * pi * radio

print(f"La longitud del perímetro es: {longitud}")




# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------