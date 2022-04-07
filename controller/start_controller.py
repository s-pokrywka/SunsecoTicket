from flask_wtf import FlaskForm
from flask import Blueprint,render_template
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
app_index=Blueprint('app_index',__name__)


class Sing_in_form(FlaskForm):
    name = StringField('Użytkownik', validators=[DataRequired()])
    password=PasswordField('Hasło',validators=[DataRequired()])
    submit = SubmitField('Zaloguj')

@app_index.route('/', methods=['GET', 'POST'])
def index():
 name = None
 password = None
 form = Sing_in_form()

 return render_template('start.html', form=form, name=name, password=password)