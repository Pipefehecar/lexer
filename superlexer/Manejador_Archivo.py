class archivo():
    """aca leo los cargo los archivos"""
    def __init__(self, nombre):
        global nombree, archivo 
        nombree=nombre
        archivo = open(nombree + ".gh", "rt")

    def dame_linea(self):
       linea=archivo.readline()
       return linea

    def numero_lineas(self):
        archivoo = open(nombree + ".gh", "rt")
        lineas = archivoo.readlines()
        archivoo.close()
        #print("leo: ", lineas)
        return len(lineas)


    def cerrar_archivo(self):
        archivo.close()

    # def imprimir_linea(self)


#n_archivo = input("Ingrese el nombre del archivo: ")
#lexer = archivo(n_archivo)
# lexer.leer_archivo()
