from flask import render_template
from src.app import app
from src.models.bibliotecario import Bibliotecario

@app.route('/bibliotecarios')
def ver_bibliotecarios():
    bibliotecarios = Bibliotecario.query.all()
    return render_template('bibliotecario.html', nombre='A', apellido='A', bibliotecarios=bibliotecarios)