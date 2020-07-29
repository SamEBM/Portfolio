# Usando FLASK
# Activar un virtual environment desde cmd: venv\Scripts\activate.bat
# Instalar: pip install Flask
# set FLASK_APP=servidor.py
# Activar la actualizacion en tiempo real: set FLASK_ENV=development

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:pagina>')
def portfolio(pagina):
    return render_template(pagina)

def escribirArchivo (datos):
    with open('venv/basedatos.txt', mode='a') as baseDatos:
        email = datos["email"]
        asunto = datos["asunto"]
        mensaje = datos["mensaje"]
        archivo = baseDatos.write(f'\n{email},{asunto},{mensaje}')

def escribirExcel (datos):
    with open('venv/basedatos.csv', mode='a', newline='') as baseDatos2:
        email = datos["email"]
        asunto = datos["asunto"]
        mensaje = datos["mensaje"]
        csv_writer = csv.writer(baseDatos2, delimiter=',', quotechar='|', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,asunto,mensaje])

@app.route('/submit_formulario', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # Convierte el formulario en un diccionario
            escribirExcel(data)
            return redirect('gracias.html') # Lo manda a la página de agradecimiento
        except Exception as err:
            return err.args
    else:
        return 'Algo salio mal, intentalo de nuevo'

# ---------------------------- PRIMER EJERCICIO EN UDEMY ----------------------------

# @app.route('/<nombreUsuario>/<int:post_id>')
# def hello(nombreUsuario = None, post_id= None):
#     return render_template('index.html', name = nombreUsuario, postID = post_id)

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/blog')
# def blog():
#     return 'Esto es un blog'