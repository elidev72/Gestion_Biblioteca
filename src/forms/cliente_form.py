from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nombre: str = StringField('Nombre', validators=[DataRequired()])
    apellido: str = StringField('Apellido', validators=[DataRequired()])
    # Boton
    enviar = SubmitField('Enviar', render_kw={'class':'button is-success'})
