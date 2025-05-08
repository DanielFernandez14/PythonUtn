"""
Perfecto! PEP 8 es la guía oficial de estilo para escribir código Python limpio y legible, mantenido por la comunidad de Python.

A continuación te doy las reglas principales organizadas por categoría, como usaría un programador profesional.

🧱 1. Formato General
Usá 4 espacios por nivel de indentación (¡nunca tabulaciones!).

Máximo 79 caracteres por línea (72 para comentarios/docstrings).

Usá líneas en blanco para separar funciones, clases y bloques lógicos.

🧑‍💻 2. Nombres de variables, funciones y clases
Funciones y variables: snake_case

python
Copiar código
mi_variable = 42
def calcular_area():
Clases: CamelCase

python
Copiar código
class MiClase:
Constantes: MAYUSCULAS_CON_GUIONES

python
Copiar código
PI = 3.14
🔗 3. Espacios en blanco
❌ Nunca antes de paréntesis, corchetes o llaves:

python
Copiar código
print("hola")  # ✅ correcto
print ("hola")  # ❌ incorrecto
❌ No pongas espacios alrededor del igual si es asignación por argumento:

python
Copiar código
def funcion(x=5):  # ✅ correcto
def funcion(x = 5):  # ❌ incorrecto
✅ Usá espacios alrededor de operadores binarios:

python
Copiar código
resultado = a + b  # ✅
resultado=a+b  # ❌
💬 4. Comentarios
Comentarios deben ser claros, concisos y en español o inglés, según el proyecto.

Comenzá las frases con mayúscula, sin omitir el #:

python
Copiar código
# Este bloque calcula el promedio
Evitá comentarios redundantes:

python
Copiar código
x = 5  # Asigna 5 a x  ❌ (esto es obvio)
📦 5. Importaciones
Siempre al principio del archivo.

Ordenadas: primero las estándar, luego las de terceros, luego las locales. Separadas por líneas en blanco:

python
Copiar código
import os
import sys

import numpy as np

import mi_modulo
Evitá from modulo import * (contamina el espacio de nombres).

🧪 6. Estructura del código
Una función debe hacer una sola cosa bien.

Si el bloque if __name__ == "__main__" está presente, debe ir al final del archivo.

python
Copiar código
if __name__ == "__main__":
    main()
🧰 7. Buenas prácticas extra
Evitá usar una letra sola como nombre de variable, salvo en bucles (i, j, etc.).

Usá is para comparar con None, no ==:

python
Copiar código
if x is None:  # ✅
if x == None:  # ❌
📘 ¿Querés verlo aplicado?
Acá un mini ejemplo respetando PEP 8:

python
Copiar código
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura

if __name__ == "__main__":
    resultado = calcular_area_rectangulo(5, 3)
    print(f"Área: {resultado}")
"""