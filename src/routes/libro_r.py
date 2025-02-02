from flask import render_template, request, redirect, url_for
from src.app import app, db
from src.models.libro import Libro
from src.forms.libro_form import LibroForm

@app.route('/libros')
def opciones_libros():
    return render_template('/libro/opciones_libros.html', nombre='A', apellido='A')

@app.route('/libros/agregar', methods=['GET', 'POST'])
def agregar_libro():
    libro = Libro()
    libro_form = LibroForm(obj=libro)
    retorno = render_template('/libro/agregar_libro.html', nombre='A', apellido='A', lf=libro_form)
    
    if request.method == 'POST':
        if libro_form.validate_on_submit():
            libro_form.populate_obj(libro)
            db.session.add(libro)
            db.session.commit()
            
            retorno = redirect(url_for('opciones_libros'))
    
    return retorno

@app.route('/libros/ver')
def ver_libros():
    libros = Libro.query.all()
    return render_template('/libro/ver_libros.html', nombre='A', apellido='A', libros=libros)
