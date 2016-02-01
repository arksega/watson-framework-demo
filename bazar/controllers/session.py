# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers

class Session(controllers.Action):
   
    def login_action(self):
        print('Login!', self.request.session.id)
        return 'Login!'

    def logout_action(self):
        print('Logout!')
        return 'Logout!'

# vim: sw=4 sts=4 et si
