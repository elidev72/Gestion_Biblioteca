from flask import render_template, request, redirect, url_for
from src.app import app, login_requerido
from src.services.prestamo_service import PrestamoService as ps, PrestamoForm
from src.models import Libro

@app.route('/libros/libro/<int:id_libro>/prestar', methods=['GET', 'POST'])
def prestar_libro(id_libro: int):
    prestamo_form = PrestamoForm()
    l: Libro = Libro.query.get_or_404(id_libro)
    retorno = render_template('/prestamo/crear_prestamo.html', id_libro=id_libro, nombre_libro=l.nombre, pf=prestamo_form)
    
    if request.method == 'POST':
        if prestamo_form.validate_on_submit():
            ps.crear_prestamo(prestamo_form=prestamo_form, id_libro=id_libro)
            retorno = redirect(url_for('detalle_libro', id=id_libro))
            
    return retorno

@app.route('/prestamos')
def historial_prestamos():
    return render_template('/prestamo/ver_prestamos.html', prestamos=ps.traer_prestamos())

@app.route('/prestamos/guardar_dato', methods=['POST'])
def guardar_dato():
    id_prestamo = request.form['id_prestamo']
    
    ps.devolver_prestamo(id_prestamo=id_prestamo)
    
    return redirect(url_for('historial_prestamos'))
