from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class LibroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    anio = IntegerField('Año', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    genero = StringField('Genero', validators=[DataRequired()])
    total = IntegerField('Libros totales', validators=[
        DataRequired(),
        NumberRange(min=1, message='Para cargar un libro al sistema debe existir al menos 1 ejemplar disponible en biblioteca')
        ])
    
    enviar = SubmitField('Enviar', render_kw={'class':'button is-success'})
