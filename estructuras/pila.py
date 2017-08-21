class nodosimple():
	"""docstring for nodosimple"""
	def __init__(self,dato,indice):
		
		self.dato = dato
		self.nodosiguiente	=  None
		self.indice = indice
class pila():
	cadenapost=""
	cadenaOrden=""
	cadenapre=""
	def __init__(self):
		self.cabeza = None
	def push(self,dato):
		#print("entro push")
		nuevo = nodosimple(dato,0)
		if self.cabeza == None:
			self.cabeza = nuevo
		else:
			nuevo.nodosiguiente = self.cabeza
			self.cabeza = nuevo

	def pop(self):
		if self.cabeza != None:
			aux = None
			aux = self.cabeza
			self.cabeza = self.cabeza.nodosiguiente
			return aux.dato
		return "null"	
	def peek(self):
		if self.cabeza != None:
			return self.cabeza.dato

	def recorrerPila(self):
		
		while self.cabeza!= None:
			print self.cabeza.dato

		 	self.cabeza = self.cabeza.nodosiguiente
	def setInOrden(self,val ):
		global cadenaOrden
		cadenaOrden = val
	def setPostOrden(self,val):
		global cadenapost
		cadenapost = val	
	def setPreOrden(self,val):
		global cadenapre
		cadenapre = val
	def recorrerOperar(self , linea):
			lineaSplit = linea.split(" ")
			contSigno = ''

			self.setInOrden(linea)
			self.ordenarPreOrden(linea)

			for x in range(len(lineaSplit)):
				if (lineaSplit[x] == "+" or lineaSplit[x] == "-" or lineaSplit[x] == "*" ):

						self.push(lineaSplit[x])
						print ( " op: " + lineaSplit[x]),
						operando = self.pop()
						print  ( "op  : " + str(operando)),
						a = self.pop()
						print  ( "num  : " + str(a)),
						b = self.pop()
						print  ( "num  : " + str(b)),
						c = 0
						if( operando == "+"):
							c = int(a) + int(b)
						elif(operando == "-"):
							c = int(b) - int(a)	
						elif(operando == "*"):
							c = int(a) * int(b)
						print  ( "respuesta  : " + str(c))	
						self.push(c)	

				else:		
					self.push(lineaSplit[x])

	def ordenarPreOrden(self,linea):
		contenedor= ""
		signo = ""
		setInOrden(linea)
		lineaSplit = linea.split(" ")
		print len(linea)
		print contenedor
		conter = 0
		for x in range(len(linea)):
			
			
			if (linea[x] == "+" or linea[x] == "-" or linea[x] == "*" ):
				signo =linea[x]
				print "operacion: "+ signo

			if linea[x].isdigit() or linea[x]==" ":
				contenedor+=linea[x]
				conter=conter+1
				
				print "contenedor "+contenedor
			if conter==2:
				contenedor += " "+signo
				conter=0
			
		print "contenedor full: "+ contenedor
	def getInOrden(self):
		return cadenaOrden
	def getPostOrden(self):
		return cadenapost
	def getPreOrden(self):
		return cadenapre

	def calcula(self,a):
		total=int(a[0])
		i=1
		while (i<len(a)):
			if (a[i]=='+'):
				if (a[i+1]=='('):
					M=self.calcula(a[i+2:len(a)-1])
					total = total+ M[0]
					i+=M[1]
				else:
					total=total+int(a[i+1])
					i=i+1
			elif (a[i]=='-'):
				if (a[i+1]=='('):
					M=self.calcula(a[i+2:len(a)-1])
					total = total- M[0]
					i+=M[1]
				else:
					total=total-int(a[i+1])
					i=i+1
			elif (a[i]=='*'):
				if (a[i+1]=='('):
					M=self.calcula(a[i+2:len(a)-1])
					total = total*M[0]
					i+=M[1]
				else:
					total=total*int(a[i+1])
					i=i+1
			elif (a[i]=='/'):
				if (a[i+1]=='('):
					M=self.calcula(a[i+2:len(a)-1])
					total = total/M[0]
					i+=M[1]
				else:
					total=total/int(a[i+1])
					i=i+1
			elif (a[i]==')'):
				break
			i+=1
		return [total,i+2]

	


# pi = pila()
# print pi.calcula("5 * (2 + 3 + 3 ) + 3")[0]
#pi.recorrerOperar("2 2 + 5 *")
# pi.recorrerOperar("2 2 +")
#pi.ordenarPreOrden("2 + 3 * 8 ( 4 + 4 )")
# print("cadena in orden: "+ pi.getInOrden())
# def recorrerOperar(self , linea):
# 		lineaSplit = linea.split(" ")



# 		for x in range(len(lineaSplit)):
# 			if (lineaSplit[x] == "+" or lineaSplit[x] == "-" or lineaSplit[x] == "*" ):
# 					self.push(lineaSplit[x])
# 					print ( " op: " + lineaSplit[x]),
# 					operando = self.pop()
# 					print  ( "op  : " + str(operando)),
# 					a = self.pop()
# 					print  ( "num  : " + str(a)),
# 					b = self.pop()
# 					print  ( "num  : " + str(b)),
# 					c = 0
# 					if( operando == "+"):
# 						c = int(a) + int(b)
# 					elif(operando == "-"):
# 						c = int(b) - int(a)	
# 					elif(operando == "*"):
# 						c = int(a) * int(b)
# 					print  ( "respuesta  : " + str(c))	
# 					self.push(c)	

# 			else:		
# 				self.push(lineaSplit[x])