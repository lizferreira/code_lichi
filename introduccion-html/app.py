#importamos de la libreria flask, la clase flask para poder construir la aplicación
from flask import Flask, render_template
#importamos requests para poder las consultas a la api
import requests
#importar shutil
import shutil

#inicializar la aplicación de Flask creando una variable y diciendole que va tener la forma de la clase Flask
app=Flask(__name__)

#crear primera ruta para que nuestra aplicación pueda ser accedida desde el navegador, la barra / indica que es la pagina principal
@app.route('/')

#esta es la función que se va ejecutar cuando ingresemos en la ruta principal
def pagina_principal():
    return "Hola! Bienvenidos a la página principal"

#ruta de imagen de la nasa
@app.route('/imagen')

def imagen():
    api_key='YqgOubxdOUoNPjXlHS301b2ji5lGTqkD3Dkgb43J'
    response=requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    data=response.json()
    image_url=data['url']
    image_response=requests.get(image_url, stream=True)

    with open('static/image.jpg', 'wb') as out_file:
        shutil.copyfileobj(image_response.raw, out_file)

    return render_template("imagen.html",image_url=image_url )

#nueva ruta
@app.route('/blog')

def blog():
    return render_template('blog.html')

#ruta index
@app.route('/index')

def index():
    return render_template("index.html")


# va al fondo porque sirve para darle funcionalidad al boton de play o compilador de arriba 
if __name__ == '__main__': 
    app.run (debug=True)
