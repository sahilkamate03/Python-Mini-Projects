from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class todoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    desc = TextAreaField('Description')
    submit = SubmitField('Add')

class UpdatetodoForm(FlaskForm):
    title = StringField('Title')
    desc = TextAreaField('Description')
    submit = SubmitField('Update')