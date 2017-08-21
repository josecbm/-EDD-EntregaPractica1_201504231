from xml.dom import minidom
import pila
import cola
import lista_doblemente_Enlazada


class archivo():
	"""docstring for operadorArchivo"""
	global pila 
	
	global practica1 
	
	pila = pila.pila()
	

	def __init__(self):
		
		self.matrizX = None
		self.matrizY = None
		self.operaciones = None
	def operadorLinea(self, linea,u,lista):
		filas = 0
		colum = 0
		matr =lista.buscarUsuarios(u).matriz 
		cola = lista.buscarUsuarios(u).cola
		xmldoc = minidom.parseString(linea)
		print ("Atributo")
		print ("----------------------")
		itemlist = xmldoc.getElementsByTagName("x")
		for i in itemlist:
		    print (i.firstChild.nodeValue)
		    filas = i.firstChild.nodeValue
		    print "----"
		    print filas

		itemlist = xmldoc.getElementsByTagName("y")
		for i in itemlist:
		    print (i.firstChild.nodeValue)
		    print "----"

		    colum=i.firstChild.nodeValue
		    print colum
		matr.crearMatriz(filas,colum)
		itemlist = xmldoc.getElementsByTagName("operacion")
		for i in itemlist:
		    #print (i.firstChild.nodeValue.strip())
		    cadena = i.firstChild.nodeValue.strip()
		    cola.add(cadena)

		  
				
		
	def operando(self,u,lista):
		cola =lista.buscarUsuarios(u).cola
		while True :

			print(""" Menu resolver operaciones
		1. Operar siguiente 
		2. Regresar
		""")
			opcion = input()

			if opcion == 1:
				#print cola.desencolar()
				operacion = cola.desencolar()
				if operacion != None:
					pila.recorrerOperar(operacion)
				else:
					print("se acabaron las operaciones amigo")

			if opcion == 2:
				break

		
		