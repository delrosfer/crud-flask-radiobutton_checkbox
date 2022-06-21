from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ContactModel(db.Model):
	__tablename__ = "contacts"

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String())
	apellidos = db.Column(db.String())
	correo_e = db.Column(db.String())
	contrasena = db.Column(db.String())
	genero = db.Column(db.String())
	pasatiempos = db.Column(db.String())
	pais = db.Column(db.String(40))

	def __init__(self, nombre, apellidos, correo_e, contrasena, genero, pasatiempos, pais):
		self.nombre = nombre
		self.apellidos = apellidos
		self.correo_e = correo_e
		self.contrasena = contrasena
		self.genero = genero
		self.pasatiempos = pasatiempos
		self.pais = pais

		def __repr__(self):
			return f"{self.nombre}:{self.apellidos}"

			