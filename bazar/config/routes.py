# -*- coding: utf-8 -*-
routes = {
    'index': {
        'path': '/',
        'options': {'controller': 'bazar.controllers.Index'},
        'priority': 2
    },
    'login': {
        'path': '/[:action]',
        'options': {'controller': 'bazar.controllers.Session'},
    }
}
# vim: sw=4 sts=4 et
