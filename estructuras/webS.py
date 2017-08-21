from flask import Flask , request
import Archivo

app = Flask("servidor Ip")



@app.route('/ServicePrueba',methods=['POST']) 
def prueba():
	
	return "gola"
@app.route('/ServiceAgregar',methods=['POST'])	
def agregarNodo():
	return "hola"

@app.route("/")
def hello2():
    return "Hello my friend!"

if __name__ == "__main__":
    app.run()


 