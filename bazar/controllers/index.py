# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers

from bazar.app import logged

class Index(controllers.Rest):

    @logged
    def GET(self):
        print('Control!')
        return 'Welcome to Watson v{0}!'.format(framework.__version__)

# vim: sw=4 sts=4 et si
