from watson import form, validators
from watson.form import fields

class Login(form.Form):
    username = fields.Text(label='Usuario', _class='form-control', required=True)
    password = fields.Password(label='Contrasena', _class='form-control', required=True, validators=[validators.Length(min=5)])
    submit = fields.Submit(value='Login', _class='btn btn-lg btn-primary btn-block', button_mode=True)
