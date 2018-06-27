from flask_wtf import Form
from wtforms.validators import Required
from wtforms.fields import StringField, SubmitField


class LoginForm(Form):
    name = StringField('Name', validators=[Required()])
    room = StringField('Chat Room', validators=[Required()])
    submit = SubmitField('Enter Chatroom')