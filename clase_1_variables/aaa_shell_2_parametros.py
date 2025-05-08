import sys

# python aaa_shell_2_parametros.py v1 v2 v3
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv)
print(type(sys.argv))
print(len(sys.argv))
print(sys.argv[1:])
 

""" 
por cmd
🔍 ¿Qué hace este código?
Este script imprime los argumentos pasados desde la línea de comandos usando sys.argv, que es una lista de strings donde:

sys.argv[0]: es el nombre del script (aaa_shell_2_parametros.py)

sys.argv[1], [2], [3]: son los valores v1, v2, v3 que vos le pasás al ejecutarlo

sys.argv: imprime la lista completa

type(sys.argv): muestra que es una lista (<class 'list'>)

len(sys.argv): cantidad total de argumentos (incluyendo el nombre del script)

sys.argv[1:]: todos los argumentos menos el nombre del script
"""