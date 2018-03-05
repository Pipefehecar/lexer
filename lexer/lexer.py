from Manejador_Archivo import archivo
import re
class analisis_lexico():
	"""aqui es el corazon de nuestro lexer"""
	def __init__(self):
		global Manejador_Archivo
		Manejador_Archivo=archivo(input("Nombre del archivo: "))
	
	def validador(self):
		for p in range(1, Manejador_Archivo.numero_lineas()):
			#print(Manejador_Archivo.dame_linea())
			lista_linea = Manejador_Archivo.dame_linea().split(" ")
			#print("tu linea: ",linea)
			#print("tu lista: ",lista_linea)
			for palabra in lista_linea:
				if re.match("esta",palabra):
					print("hay coincidencia")
				else:
					print("que miras cv?")