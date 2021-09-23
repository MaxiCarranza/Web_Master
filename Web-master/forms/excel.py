from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

class ExcelForm(FlaskForm):
    excel_file = FileField(validators=[FileRequired()])
    submit = SubmitField('Cargar')