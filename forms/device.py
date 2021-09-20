from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired

class HistorialForm(FlaskForm):
    sap_id = StringField('Ingresar SAP_ID', validators=[
        DataRequired('Se requiere este campo'), 
        validators.Length(min=10, max=21, message="Min. 10 y Max. 21")])
    submit = SubmitField('Consultar')