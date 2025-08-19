from flask_wtf import FlaskFrom
from wtforms import StringField, SubmitField

class MyForm(FlaskFrom):
  name = StringField('Name')
  submit = StringField('Submit')