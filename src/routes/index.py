from flask import render_template
from src.app import app

@app.route('/')
def inicio():
    return render_template('index.html')