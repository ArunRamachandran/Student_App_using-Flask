from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField, validators
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

class LoginForm(Form):
	openid = StringField('openid', validators=[InputRequired()])
	remember_me = BooleanField('remember_me', default=False)
