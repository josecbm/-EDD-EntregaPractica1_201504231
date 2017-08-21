import json

class nodolista():
	def __init__(self, ip , mascara ):
		self.carnet = None
		self.mascara = mascara
		self.ip = ip
		self.siguiente = None 


class listaNodo():
	"""docstring for lista"""
	def __init__(self):
		self.cabeza = None 
	def add(self,ip,mascara):
		
		nuevoNodo = nodolista(ip,mascara)


		if self.cabeza == None :
			self.cabeza = nuevoNodo
		else:

			nodoTemporal = self.cabeza.siguiente

			self.cabeza.siguiente = nuevoNodo
			nuevoNodo.siguiente = nodoTemporal



	def recorrer(self):
		temporal = self.cabeza
		
		while temporal!=None:
			
			print temporal.carnet
			temporal = temporal.siguiente
			
	def recorre2(self):
		temporal = self.cabeza.siguiente
		
		
		while temporal!=None:
			
			print temporal.ip
			temporal = temporal.siguiente
		print self.cabeza.ip	
	def recorre1(self):
		temporal = self.cabeza.siguiente
		print self.cabeza.ip
		
		while temporal!=None:
			
			print temporal.ip
			temporal = temporal.siguiente
		
	def buscarip(self,ip):
		temporal = self.cabeza.siguiente
	
		if self.cabeza.ip == ip :
			return True
		else:
			while temporal!=None:
			
				if  temporal.ip == ip:
					return True
				temporal = temporal.siguiente

	def graficar(self):
		import os
		archi=open('nodoCreado.txt','w')
		rchi=open('nodoCreado.txt','a')
		archi.write('digraph G {')		
		temporal = self.cabeza.siguiente
		tempP = str(self.cabeza.ip)
		archi.write('"'+ tempP+'"'+','+'"'+str(temporal.mascara)+'"')
		while temporal!=None:
			temp = str(temporal.ip)
			archi.write("->"+'"'+temp+'"'+','+'"'+str(temporal.mascara)+'"')
			temporal = temporal.siguiente
		archi.write('}')

		import os
		
		dotPath = "dot"
		fileInputPath="nodoCreado.txt"
		fileOutputPath="nodoCreado.png"
		
		print dotPath
		print fileOutputPath
		print fileInputPath
		tParam = " -Tpng "
		tOParam = " -o "
		tuple = (dotPath +tParam+ fileInputPath+tOParam+fileOutputPath)
		print tuple 
		os.system(tuple)

	def convertirJSON(self):
		pythonDictionary=''
		pythonDictionary +='['
		n = "nodo"
		ip ='"'+"ip"+'"'
		mascara = '"'+"mascara"+'"'
		c='"'
		cont = 0
		print mascara
		temporal = self.cabeza.siguiente
		
		
		while temporal!=None:
			cont = cont + 1
			pythonDictionary += '{'+c+n+c+':'+'"'+n+str(cont)+'"'+','+ip+':'+c+temporal.ip+c+','+mascara+':'+c+temporal.mascara+c+'}'
			
			pythonDictionary+=','
			temporal = temporal.siguiente
		cont = cont +1
		pythonDictionary+= '{'+c+n+c+':'+'"'+n+str(cont)+'"'+','+ip+':'+c+self.cabeza.ip+c+','+mascara+':'+c+self.cabeza.mascara+c+'}'
		pythonDictionary+=']'
		dictionaryToJson = json.dumps(pythonDictionary)	
		
		with open('datosfinales.json', 'w') as file:
			
   			 json.dump(pythonDictionary, file)
   		return dictionaryToJson	 
				



# l = listaNodo()
# l.add("192.168.1.1","255.255.255")
# l.add("192.168.1.2","255.255.255")
# l.add("192.168.1.3","255.255.255")
# l.add("192.168.1.4","255.255.255")
# print l.convertirJSON()
# print l.buscarip("192.168.1.1")
#l.recorrer()
#l.recorre2()
#print l.buscarip(919191)
# #l.graficar()
# print temporal.ip
# 			pythonDictionary += {'ip':"'"+temporal.ip+"'",'mascara':"'"+temporal.mascara+"'"}
# 			if temporal.siguiente==None:
# 				pythonDictionary+= ,
# 			temporal = temporal.siguiente
# 		dictionaryToJson = json.dumps(pythonDictionary)
# 		print dictionaryToJson	
