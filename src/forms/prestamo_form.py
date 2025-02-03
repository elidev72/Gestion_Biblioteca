from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class PrestamoForm(FlaskForm):
    cliente_id: str = IntegerField('ID cliente', validators=[DataRequired()])

    enviar = SubmitField('Enviar', render_kw={'class':'button is-success'})