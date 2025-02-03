from flask import render_template, redirect, url_for, request, session
import bcrypt
from src.app import app
from src.services.bibliotecario_service import BibliotecarioService as bs

@app.route('/')
def inicio():
    """
    retorno = redirect(url_for('login'))
    
    if 'logged_in' in session:
        retorno = render_template('index.html', nombre=session['nombre'], apellido=session['apellido'])
    
    return retorno
    """
    return render_template('index.html', nombre='A', apellido='A')

@app.route('/login', methods=['GET', 'POST'])
def login():
    retorno = render_template('login.html', login_page=True)
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        clave = request.form['clave']

        bibliotecario = bs.traer_por_nombre_y_apellido(nombre=nombre, apellido=apellido)
        
        if bibliotecario and bcrypt.checkpw(clave.encode('utf-8'), bibliotecario.clave.encode('utf-8')):
            session['logged_in'] = True
            session['nombre'] = nombre
            session['apellido'] = apellido
            session['id'] = bibliotecario.id
            retorno = redirect(url_for('inicio'))

    return retorno

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
