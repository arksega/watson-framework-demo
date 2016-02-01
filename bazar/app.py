# -*- coding: utf-8 -*-
from watson.framework import applications
from bazar.config import config

def logged(func):
    def inner(self, *args, **kargs):
        print('Decorated', self)
        print(self.request.session['salt'])
        if not self.request.session['salt']:
            self.redirect('/login')
        return func(self, *args, **kargs)
    return inner

application = applications.Http(config)

# vim: sw=4 sts=4 et si
