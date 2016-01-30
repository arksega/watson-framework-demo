# -*- coding: utf-8 -*-
from watson import framework
from bazar.controllers.index import Index


class TestSuiteIndex(object):
    def test_get(self):
        index = Index()
        assert index.GET() == 'Welcome to Watson v{0}!'.format(framework.__version__)
