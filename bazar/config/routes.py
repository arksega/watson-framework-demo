# -*- coding: utf-8 -*-
routes = {
    'index': {
        'path': '/',
        'options': {'controller': 'bazar.controllers.Index'}
    },
    'login': {
        'path': '/login',
        'options': {
            'controller': 'bazar.controllers.Login',
            'action': 'login'
        }
    }
}
# vim: sw=4 sts=4 et
