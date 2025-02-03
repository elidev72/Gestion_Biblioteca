from flask import render_template
from src.app import app
from src.services.bibliotecario_service import BibliotecarioService as bs

@app.route('/bibliotecarios')
def ver_bibliotecarios():
    return render_template('bibliotecario.html', nombre='A', apellido='A', bibliotecarios=bs.traer_todos())
