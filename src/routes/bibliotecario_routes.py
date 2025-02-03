from flask import render_template
from src.app import app
from src.repositories.bibliotecario_repository import BibliotecarioRepository as br

@app.route('/bibliotecarios')
def ver_bibliotecarios():
    return render_template('bibliotecario.html', nombre='A', apellido='A', bibliotecarios=br.traer_todos())
