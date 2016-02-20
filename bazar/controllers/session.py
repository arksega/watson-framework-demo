# -*- coding: utf-8 -*-
from watson.framework import controllers
from watson import framework
from bazar.db import User
from bazar import forms
import hashlib, binascii
import sqlalchemy

class Login(controllers.Rest):
   
    def GET(self):
        if self.request.session['logged']:
            self.redirect('index')
        login = forms.Login(action='/login', _class='form-signin')
        login.data = self.redirect_vars
        print(login.errors)
        return {'form': login}

    def POST(self):
        login = forms.Login(action='/login', _class='form-signin')
        login.data = self.request.post
        if login.is_valid():
            db = self.container.get('db')
            try:
                user = db.query(User).filter(User.name == login.username).one()
            except sqlalchemy.orm.exc.NoResultFound:
                self.flash_messages.add('Tu nombre de usuarion no esta registrado', namespace='danger')
                return {'form': login}
            print(user.password)
            dk = hashlib.pbkdf2_hmac('sha256', login.password.encode(), user.salt.encode(), 100000)
            password = binascii.hexlify(dk)
            print(password, user.password)
            if password == user.password.encode():
                print('Saving', self.request.session)
                self.request.session['logged'] = True
                self.flash_messages.add('Bienvenido!')
                self.redirect('index')
            else:
                self.flash_messages.add('El usuario y contraseña prorcionados no coinciden')
        else:
            for field in login.errors.keys():
                for ms in login.errors[field]['messages']:
                    self.flash_messages.add('{} {}'.format(field, ms))
            #self.redirect('login')
        return {'form': login}

class Logout(controllers.Rest):

    def GET(self):
        self.request.session['logged'] = False
        self.redirect('index')

# vim: sw=4 sts=4 et si
