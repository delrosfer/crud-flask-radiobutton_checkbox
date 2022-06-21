from flask import Flask, render_template, request, redirect
from models import db,ContactModel
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
	db.create_all()

@app.route('/create', methods = ['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create.html')

	if request.method == 'POST':
		pasatiempo = request.form.getlist('pasatiempos')
		pasatiempos = ','.join(map(str, pasatiempo))
		nombre = request.form['nombre']
		apellidos = request.form['apellidos']
		correo_e = request.form['correo_e']
		contrasena = request.form['contrasena']
		genero = request.form['genero']
		pasatiempos = pasatiempos
		pais = request.form['pais']

		contacts = ContactModel(
			nombre = nombre,
			apellidos = apellidos,
			correo_e = correo_e,
			contrasena = contrasena,
			genero = genero,
			pasatiempos = pasatiempos,
			pais = pais
		)
		db.session.add(contacts)
		db.session.commit()
		return redirect('/')

@app.route('/' , methods = ['GET'])
def RetrieveList():
	contacts = ContactModel.query.all()
	return render_template('index.html', contacts = contacts)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])

def update(id):
	contact = ContactModel.query.filter_by(id=id).first()

	if request.method == 'POST':
		db.session.delete(contact)
		db.session.commit()
		if contact:
			pasatiempo = request.form.getlist('pasatiempos')
			#pasatiempos = ','.join(map(str, pasatiempo))
			pasatiempos = ",".join(map(str, pasatiempo))
			nombre = request.form['nombre']
			apellidos = request.form['apellidos']
			correo_e = request.form['correo_e']
			contrasena = request.form['contrasena']
			genero = request.form['genero']
			pasatiempos = pasatiempos
			pais = request.form['pais']

			contact = ContactModel(
				nombre = nombre,
				apellidos = apellidos,
				correo_e = correo_e,
				contrasena = contrasena,
				genero = genero,
				pasatiempos = pasatiempos,
				pais = pais
			)
			db.session.add(contact)
			db.session.commit()
			return redirect('/')
		return f"El contacto con id = {id} No existe"

	return render_template('update.html', contact = contact)

@app.route('/<int:id>/delete', methods=['GET', 'POST'])

def delete(id):
	contacts = ContactModel.query.filter_by(id=id).first()
	if request.method == 'POST':
		if contacts:
			db.session.delete(contacts)
			db.session.commit()
			return redirect('/')
		abort(404)
		#return redirect('/')
	return render_template('delete.html')

app.run(host='localhost', port=5000)