import json
import nodo 
import os 
from xml.dom import minidom
import ctypes, sys,traceback, types
import cola
import colaMensaje
class archivo():


	def setCol(self,val):
		global col
		col = val 
	def setColamen(self, val):
		global colaMen
		colaMen = val 
	def getCol(self):
		return col
	def getColamen(self):
		return colaMen
	def leerArchivoNodo(self,cadena):
		nuevoNodo= nodo.listaNodo()
		print cadena	
		with open(cadena) as file:
			data = json.load(file)

			for data in data:

				print(data.get('nodos').get('local'))
				print(data.get('nodos').get('mascara'))
				#self.cambiarip(data.get('nodos').get('local'),data.get('nodos').get('mascara'))

				#print "________________________________"
				contenedor =data.get('nodos').get('nodo')
			for contenedor in contenedor:
				ip= contenedor.get('ip')
				mascara = contenedor.get('mascara')

				nuevoNodo.add(ip,mascara)
				#print(contenedor.get('ip'))
				#print(contenedor.get('mascara'))
				#print "______________________"

		return nuevoNodo

	def leerArchivoXml(self,cadena):

		#__________________________ cambiar para lo de operar
		col = cola.listaCola()
		colaMen = colaMensaje.listaColaMensaje()

		archivo = open(cadena, "r") 
		cadena= archivo.read()
		xmldoc = minidom.parseString(cadena)
		itemlist = xmldoc.getElementsByTagName("IP")
		for i in itemlist:
		    print ("ip= "+i.firstChild.nodeValue.strip())
		    col.add(i.firstChild.nodeValue.strip())
		itemlist = xmldoc.getElementsByTagName("texto")
		for i in itemlist:
		    print ("texto= "+i.firstChild.nodeValue.strip())
		    colaMen.add(i.firstChild.nodeValue.strip())
		colaMen.recorrer()
		col.recorrer()
		colaMen.generarJSON()

		return "si se pudo"

	def is_admin(self):
	    try:
	        return ctypes.windll.shell32.IsUserAnAdmin()
	    except:
	        return False

		if is_admin():
		    # Code of your program here

		    return True 
		else:
		    # Re-run the program with admin rights
		    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
		    is_admin()

	def cambiarip(self,ip,mascara):
		if not admin.isUserAdmin():
			admin.runAsAdmin()
			os.system('netsh interface ip set address name="Wi-Fi" source=static addr='+ip+' mask='+mascara+' gateway=192.168.1.1 store=persistent')
		
		#print "entro"
	


a = archivo()
# a.leerArchivoNodo("C:\Users\jose_\Documents\universidad\segundoSemestre2017\estructuras\practica1\prueba.json")
# a.getNodo().convertirJSON()
#a.cambiarip("192.168.1.1","255.255.255.0")
a.leerArchivoXml("C:\Users\jose_\Documents\universidad\segundoSemestre2017\estructuras\practica1\pruebaxml.xml")
#netsh interface ip set address name="Wi-Fi" source=static addr=192.168.1.14 mask=255.255.255.0 gateway=192.168.1.1 store=persistent