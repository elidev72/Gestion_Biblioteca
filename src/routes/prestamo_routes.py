from flask import render_template, request, redirect, url_for
from src.app import app
from src.utils import login_requerido
from src.services.prestamo_service import PrestamoService as ps, PrestamoForm
from src.models import Libro

@app.route('/libros/libro/<int:id_libro>/prestar', methods=['GET', 'POST'])
@login_requerido
def prestar_libro(id_libro: int):
    prestamo_form = PrestamoForm()
    l: Libro = Libro.query.get_or_404(id_libro)
    retorno = render_template('/prestamo/crear_prestamo.html', id_libro=id_libro, nombre_libro=l.nombre, pf=prestamo_form)
    
    if request.method == 'POST':
        if prestamo_form.validate_on_submit():
            try:
                ps.crear_prestamo(prestamo_form=prestamo_form, id_libro=id_libro)
            except Exception as e:
                print(f'Error: {e}')
            retorno = redirect(url_for('detalle_libro', id=id_libro))
            
    return retorno

@app.route('/prestamos')
@login_requerido
def historial_prestamos():
    return render_template('/prestamo/ver_prestamos.html', prestamos=ps.traer_prestamos())

@app.route('/prestamos/guardar_dato', methods=['POST'])
def guardar_dato():
    id_prestamo = request.form['id_prestamo']
    
    try:
        ps.devolver_prestamo(id_prestamo=id_prestamo)
    except Exception as e:
        print(f'Error: {e}')
    
    return redirect(url_for('historial_prestamos'))
