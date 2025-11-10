from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def ruta_principal():
    return render_template("inicio.html")

@app.route('/estudiantes')
def estudiantes():
    return render_template("estudiantes.html")







# para poder usar mi boton de play

if __name__=='__main__':
    app.run(debug=True)