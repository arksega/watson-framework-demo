# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers


class Index(controllers.Rest):
    def GET(self):
        print('Control!')
        return 'Welcome to Watson v{0}!'.format(framework.__version__)
