from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from src.utils import cliente_existe

class PrestamoForm(FlaskForm):
    cliente_id: str = IntegerField('ID cliente', validators=[DataRequired()])
    cantidad_dias_de_prestamo: str = IntegerField('Cantidad total de días de prestamo', validators=[
        DataRequired(),
        NumberRange(min=1, message='La cantidad de días de días debe ser mayor a 0')
        ])

    enviar = SubmitField('Enviar', render_kw={'class':'button is-success'})
    
    def validate_cliente_id(self, field):
        if not cliente_existe(field.data):
            raise ValidationError('El ID de cliente no existe en el sistema.')
