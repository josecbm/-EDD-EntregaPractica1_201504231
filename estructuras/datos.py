import nodo
class nodolista():
	def __init__(self,local , mascara , nodoDatos):
		self.local = local	
		self.mascara = mascara 
		self. nodoDatos = nodoDatos
		self.siguiente = None 


class lista():
	"""docstring for lista"""
	def __init__(self):
		self.cabeza = None 
	def add(self,local , mascara):
		nod = nodo.listaNodo()
		nuevoNodo = nodolista(local, mascara , nod)


		if self.cabeza == None :
			self.cabeza = nuevoNodo
		else:

			nodoTemporal = self.cabeza.siguiente

			self.cabeza.siguiente = nuevoNodo
			nuevoNodo.siguiente = nodoTemporal



	def recorrer(self):
		temporal = self.cabeza
		
		while temporal!=None:
			print temporal.local
			temporal = temporal.siguiente

# listadat =lista()
# listadat.add("192.160","255.255")
# listadat.add("192.161","255.255")
# listadat.add("192.162","255.255")
# listadat.add("192.163","255.255")
# listadat.add("192.164","255.255")
# listadat.add("192.175","255.255")
# listadat.recorrer()



		
