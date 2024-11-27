from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pizzeria'

mysql = MySQL(app)

# Configuración secreta
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos')
def datos():
    return render_template('productos.html')

@app.route('/contacto')
def contacto():
    return render_template('contactos.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    if request.method == 'POST':
        nombre = request.form.get('nombre')  
        apellido = request.form.get('apellido')
        direccion = request.form.get('direccion')
        cantidad = request.form.get('cantidad')
        tipo = request.form.get('tipo')
        telefono = request.form.get('telefono')

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO datos (nombre, apellido, direccion, cantidad, tipo, telefono) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellido, direccion, cantidad, tipo, telefono))
        mysql.connection.commit()
        cur.close()
        
        
        
        return redirect(url_for('index'))
    return render_template('pedido.html')

@app.route('/editar_contacto')
def editar_contacto():
    return "Editar contacto"

if __name__ == '__main__':
    app.run(port=3000, debug=True)
