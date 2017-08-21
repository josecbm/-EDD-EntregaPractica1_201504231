from flask import Flask , request
import Archivo
import nodo


app = Flask("servidor")
archivoNodo = Archivo.archivo()
nodoGeneral=''

def setNodoGeneral(self,nodo):
	global nodoGeneral
	nodoGeneral = nodo
@app.route('/ServicePrueba',methods=['POST']) 
def prueba():
	print "entra"
	cadena= str(request.form['url'])
	nodoIps =archivoNodo.leerArchivoNodo(cadena)
	nodoIps.graficar()
	
	return nodoIps.convertirJSON()
	
# @app.route('/Conectar', methods=['GET'])
# def conec():
# 	carnet = "201504231"
# 	return carnet
@app.route('/serviceagregarmensaje',methods=['POST']) 
def agregarMensaje():
	print "entra"
	p= str(request.form['cadena'])
	print p
	nodoMensaje =archivoNodo.leerArchivoXml(p)
	
	return "Se agregaron mensajes"


@app.route("/")
def hello2():
    return "Hello papi!"

@app.route("/conectado", methods=['GET'])
def conectado():
    ip = str(request.form['ip'])
    print ip
    respuesta = getNodoGeneral().buscarip(ip)
    if respuesta :
    	return True
    else:
    	return False 
@app.route('/ServiceAgregarNodo',methods=['POST'])
def agregarNodo():

	 
	url	 = str(request.form['url'])	
	cont = archivoNodo.leerArchivoNodo(url)
	cont.recrecorre2()
	return "True"

def getNodoGeneral(self):
	return nodoGeneral
	
# @app.route('/serviceObtenerdashboard')
# def obtenerDash():
# 	archivo = open("datos.json", "r") 
# 	contenido = archivo.read()
# 	return contenido
@app.route('/servicep')
def p():
	print "entra"
 	nodoIps =archivoNodo.leerArchivoXml("C:\Users\jose_\Documents\universidad\segundoSemestre2017\estructuras\practica1\pruebaxml.xml")
 	
 	return "true"
	


@app.route('/ServiceAgregarOperacion')
def agregarOperacion():

	return True 

# @app.route('/ServiceObtenerNodo')
# def obtenerNodo():

# 	return "nodo"
# @app.route('/saludo/<nombre>',methods=['POST'])
# def saludo(nombre):
#     return 'Hola ' + nombre + '!!!'

if __name__ == "__main__":
    app.run(debug=True) 