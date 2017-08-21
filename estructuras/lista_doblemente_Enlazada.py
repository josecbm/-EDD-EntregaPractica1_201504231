
class nodolista():
	def __init__(self,ip,mascara):
		self.ip = ip
		self.mascara = mascara
		self.carnet = None
		self.siguiente = None
		self.anterior = None
class lista():

	
	def __init__(self):
		self.cabeza = None
	def add(self,ip,mascara):
		nuevoNodo = nodolista(ip,mascara) 

		if self.cabeza == None:
			nuevoNodo.siguiente = nuevoNodo
			nuevoNodo.anterior = nuevoNodo
			self.cabeza = nuevoNodo
			bandera = True
			
		else:
			nodoTemporal = self.cabeza.anterior

			self.cabeza.anterior = nuevoNodo
			nuevoNodo.anterior = nodoTemporal
			nuevoNodo.siguiente = self.cabeza
			nodoTemporal.siguiente =nuevoNodo

		return True

	def addCola(self,usuario,objeto):
		buscarUsuarios(usuario).cola = objeto
	

	def recorrer(self):
		temporal = self.cabeza.anterior
		print self.cabeza.usuario
		print self.cabeza.passw	
		while temporal!=self.cabeza:
			print temporal.usuario
			print temporal.passw
			temporal = temporal.anterior

	def buscar(self,us):
		if self.cabeza.usuario== us :
			var = temporal
			return var
		while temporal!=self.cabeza:
			if temporal.usuario== us :
				return temporal
			else:return False
			temporal = temporal.anterior

	
	def recorrerIp(self):
		temporal = self.cabeza.anterior
		primero = self.cabeza.ip+"->"
		print primero,
		while temporal!=self.cabeza:
			var = temporal.ip+"->"
			print var,
			temporal = temporal.anterior
		print ""

	def buscarIp(self, ip):
		print ip 
		
		if self.cabeza.anterior!=None:
			temporal = self.cabeza.anterior
		else: 
			return "algo"
		
		primero = self.cabeza.ip
		if primero == usua:
			return temporal
		while temporal!=self.cabeza:
			var = temporal.usuario
			if (var == usua ):
				return temporal
			else:
				return None
			temporal = temporal.anterior

			
	def recorrerMascara(self):
		temporal = self.cabeza.anterior
		print self.cabeza.mascara
		while temporal!=self.cabeza:

			print temporal.mascara
			temporal = temporal.anterior		
	
listanueva = lista()
listanueva.add("291.168.1.1","255.255.255.0")
listanueva.add("291.168.1.2","255.255.255.0")
listanueva.add("291.168.1.3","255.255.255.0")
listanueva.recorrerIp()
#listanueva.add("nowell3","123")
#listanueva.add("nowell4","123")
#print listanueva.buscarUsuarios("nowell4").passw