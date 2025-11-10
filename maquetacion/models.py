from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#crear nuestro modelo de tabla

class Alumnos(db.Model):
    id_alumno= db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apellido=db.Column(db.String(55))
    edad=db.Column(db.Integer)
    colegio=db.Column(db.String(100))