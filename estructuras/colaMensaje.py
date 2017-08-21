import pila
import json
class nodoLista(object):
	"""docstring for listaCola"""
	def __init__(self,mensaje):
		
		self.mensaje =mensaje
			 
		self.siguiente = None
		self.aux = None
class listaColaMensaje():
	global listapila
	listapila = pila.pila()

	def __init__(self):
		self.cabeza = None
	def add(self , mensaje):
		nuevoNodo = nodoLista(mensaje)

		if self.cabeza == None:
			nuevoNodo.siguiente = None
			self.cabeza = nuevoNodo
		else:
			self.aux = self.cabeza
			while self.aux.siguiente!=None:
				self.aux = self.aux.siguiente
			self.aux.siguiente=nuevoNodo
			
	def recorrer(self):
		pythonDictionary=''
		pythonDictionary +='['
		self.aux = self.cabeza
		while self.aux!=None:
			print self.aux.mensaje
			#listapila.recorrerOperar(self.au)
			self.aux = self.aux.siguiente
	def desencolar(self):
		if self.cabeza!=None:
			aux = self.cabeza
			self.cabeza = self.cabeza.siguiente
			return aux.mensaje
	def generarJSON(self):
		pythonDictionary=''
		pythonDictionary +='['		
		self.aux = self.cabeza
		while self.aux!=None:
			print self.aux.mensaje
			pythonDictionary += '{'+'"'+"enOrden"+'"'+':'+'"'+self.aux.mensaje+'"''}'
			if self.aux.siguiente is not None:
				pythonDictionary+=','
			
			#listapila.recorrerOperar(self.aux.mensaje)
			self.aux = self.aux.siguiente
			dictionaryToJson = json.dumps(pythonDictionary)	
		with open('datosfinales3.json', 'w') as file:
			
   			 json.dump(pythonDictionary, file)
   		return dictionaryToJson	 

