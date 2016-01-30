# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Login(controllers.Action):
    def login_action(self):
        print('Login!')
        return 'Welcome to Watson v{0}!'.format(framework.__version__)

    def logout_action(self):
        print('Logout!')
        return 'Welcome to Watson v{0}!'.format(framework.__version__)
