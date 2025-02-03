from flask import render_template, request, redirect, url_for
from src.app import app
from src.repositories.libro_repository import LibroRepository as lr, LibroForm

@app.route('/libros')
def opciones_libros():
    return render_template('/libro/opciones_libros.html', nombre='A', apellido='A')

@app.route('/libros/agregar', methods=['GET', 'POST'])
def agregar_libro():
    libro_form = LibroForm()
    retorno = render_template('/libro/agregar_libro.html', nombre='A', apellido='A', lf=libro_form)
    
    if request.method == 'POST':
        if libro_form.validate_on_submit():
            lr.agregar_libro(libro_form=libro_form)
            retorno = redirect(url_for('opciones_libros'))
    
    return retorno

@app.route('/libros/ver')
def ver_libros():
    return render_template('/libro/ver_libros.html', nombre='A', apellido='A', libros=lr.traer_todos())
