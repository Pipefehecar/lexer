from Manejador_Archivo import archivo
from lexer import analisis_lexico

analisis_lexicog = analisis_lexico()
analisis_lexicog.validador()

#lexer = archivo(input("Nomnbre del archivo: "))
#print("el nombre de su arc: ",lexer.nombre_archivo)
#print("lineas: ",lexer.numero_lineas())

#for x in range(1, lexer.numero_lineas()):
	#print (lexer.dame_linea())
