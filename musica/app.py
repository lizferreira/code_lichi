# importar de la libreria flas, la clase Flask
from flask import Flask, render_template

# inicializa la aplicación de flask, con la forma de la clase Flask
app=Flask(__name__)

# pagina de inicio
@app.route('/')
def principal():
    return render_template('inicio.html')
# template de base
@app.route('/base')
def base():
    return render_template('base.html')
# vista de pagina de artistas favoritos
@app.route('/artistas')
def artistas():
    return render_template('artistas.html')
# vista de pagina de canciones favoritas
@app.route('/canciones')
def canciones():
    return render_template('canciones.html')

# boton play
if __name__=='__main__':
    app.run(debug=True)
