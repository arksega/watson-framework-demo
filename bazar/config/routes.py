# -*- coding: utf-8 -*-
routes = {
    'index': {
        'path': '/',
        'options': {'controller': 'bazar.controllers.Index'},
        'priority': 2
    },
    'login': {
        'path': '/login',
        'options': {'controller': 'bazar.controllers.Login'},
    },
    'logout': {
        'path': '/logout',
        'options': {'controller': 'bazar.controllers.Logout'},
    }
}
# vim: sw=4 sts=4 et
