import pila
class nodoLista(object):
	"""docstring for listaCola"""
	def __init__(self,ipdestino):
		
		self.ipdestino =ipdestino
			 
		self.siguiente = None
		self.aux = None
class listaCola():
	global listapila
	listapila = pila.pila()

	def __init__(self):
		self.cabeza = None
	def add(self , ipdestino):
		nuevoNodo = nodoLista(ipdestino)

		if self.cabeza == None:
			nuevoNodo.siguiente = None
			self.cabeza = nuevoNodo
		else:
			self.aux = self.cabeza
			while self.aux.siguiente!=None:
				self.aux = self.aux.siguiente
			self.aux.siguiente=nuevoNodo
			
	def recorrer(self):
		self.aux = self.cabeza
		while self.aux!=None:
			print self.aux.ipdestino
			#listapila.recorrerOperar(self.au)
			self.aux = self.aux.siguiente
	def desencolar(self):
		if self.cabeza!=None:
			aux = self.cabeza
			self.cabeza = self.cabeza.siguiente
			return aux.ipdestino

	def generarJSON(self):
		pythonDictionary=''
		pythonDictionary +='['		
		self.aux = self.cabeza
		while self.aux!=None:
			print self.aux.dato
			pythonDictionary += '{'+'"'+"ipmensaje"+'"'+':'+'"'+self.aux.dato+'"''}'
			if self.aux.siguiente is not None:
				pythonDictionary+=','
			
			#listapila.recorrerOperar(self.aux.dato)
			self.aux = self.aux.siguiente
		with open('datosfinales2.json', 'w') as file:
			
   			 json.dump(pythonDictionary, file)
   		return dictionaryToJson	 
			

# listita = listaCola()
# listita.add("192.158.1.1","1 + 20 * 3 - 20")
# listita.add("192.158.1.2","1 + 20 * 3 - 20")
# listita.add("192.158.1.3","1 + 20 * 3 - 20")
# listita.add("192.158.1.4","1 + 20 * 3 - 20")

#listita.add("2")
#listita.add("3")
#listita.add("4")
#listita.recorrer()