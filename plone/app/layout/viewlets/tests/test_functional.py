# -*- coding: utf-8 -*-
"""Functional Doctests for plone.app.discussion.

   These test are only triggered when Plone 4 (and plone.testing) is installed.
"""
    PLONE_APP_CONTENTTYPES_FUNCTIONAL_TESTING
from plone.app.contenttypes.testing import \
    from plone.testing import layered

import doctest
import unittest


optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
normal_testfiles = [
    'history.txt',
]


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     ),
                layer=PLONE_APP_CONTENTTYPES_FUNCTIONAL_TESTING)
        for test in normal_testfiles])
    return suite
