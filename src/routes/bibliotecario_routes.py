from flask import render_template
from src.app import app
from src.utils import login_requerido
from src.services.bibliotecario_service import BibliotecarioService as bs

@app.route('/bibliotecarios')
@login_requerido
def ver_bibliotecarios():
    return render_template('bibliotecario.html', bibliotecarios=bs.traer_todos())
