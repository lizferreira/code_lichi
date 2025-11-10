from models import Alumnos, db

from flask import Flask

app=Flask('app')

# configuracion de la base de datos
# crea la base de datos

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# se coloca para optimizar procesos, para no rastrear

# inicializar la base de datos

db.init_app(app)

# creacion de la base de datos

with app.app_context():
    # db.create_all()
    alumno_agregar=Alumnos(nombre='Liz', apellido='Ferreira', edad='26', colegio='CNTP')
    db.session.add(alumno_agregar)
    db.session.commit()
    