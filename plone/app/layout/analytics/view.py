from zope.interface import implements
from zope.viewlet.interfaces import IViewlet

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner


class AnalyticsViewlet(BrowserView):
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(BrowserView, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        pass

    def render(self):
        """render the webstats snippet"""
        ptool = getToolByName(aq_inner(self.context), "portal_properties")
        snippet = ptool.site_properties.webstats_js
        return snippet

