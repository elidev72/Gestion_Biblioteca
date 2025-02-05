from flask import render_template
from src.app import app

@app.errorhandler(404)
def pagina_no_encontrada(error) -> str:
    return render_template('error.html', numero=404, error=error), 404

@app.errorhandler(500)
def error_interno(error) -> str:
    return render_template('error.html', numero=500, error=error), 500
