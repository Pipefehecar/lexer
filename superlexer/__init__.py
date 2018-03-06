from Manejador_Archivo import archivo
from logica_lexer import Lexer
name = input("ingrese el nombre del archivo :\n")
f = archivo(name)
l = Lexer()
for x in range(0,f.numero_lineas()):
	data = f.dame_linea()
	print(l.prueba(data))