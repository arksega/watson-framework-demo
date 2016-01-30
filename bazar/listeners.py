# -*- coding: utf-8 -*-
from watson.di import ContainerAware
from watson.framework import listeners

class SessionListener(listeners.Base, ContainerAware):
    def __call__(self, event):
        print('Match!')
        return event

class Dispacher(listeners.DispatchExecute):
    def __init__(self, *args, **kwargs):
        super(Dispacher, self).__init__(self, *args, **kwargs)

    def __call__(self, event):
        print('Dispatch!')
        print(self.determine_controller(event))
        return event

# vim: sw=4 sts=4 et ai
