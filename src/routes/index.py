from flask import render_template, redirect, url_for, request, session, flash
import bcrypt
from src.app import app
from src.models.bibliotecario import Bibliotecario

@app.route('/')
def inicio():
    retorno = redirect(url_for('login'))
    
    if 'logged_in' in session:
        retorno = render_template('index.html', nombre=session['nombre'], apellido=session['apellido'])
    
    return retorno

@app.route('/login', methods=['GET', 'POST'])
def login():
    retorno = render_template('login.html', login_page=True)
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        clave = request.form['clave']

        bibliotecario = Bibliotecario.query.filter_by(nombre=nombre, apellido=apellido).first()
        
        if bibliotecario and bcrypt.checkpw(clave.encode('utf-8'), bibliotecario.clave.encode('utf-8')):
            session['logged_in'] = True
            session['nombre'] = nombre
            session['apellido'] = apellido
            session['id'] = bibliotecario.id
            flash('Inicio de sesión exitoso', 'success')
            retorno = redirect(url_for('inicio'))
        else:
            flash('Credenciales incorrectas', 'danger')

    return retorno

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))
