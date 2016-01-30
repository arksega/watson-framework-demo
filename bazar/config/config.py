# -*- coding: utf-8 -*-
from bazar.config.routes import routes
from watson.framework import events

events = {
    events.ROUTE_MATCH: [
        ('bazar.listeners.SessionListener', 2, False)
    ],
    events.DISPATCH_EXECUTE: [
        ('bazar.listeners.Dispacher', 1, False)
    ]
}

debug = {
    'enabled': True
}

# vim: sw=4 sts=4 et ai
