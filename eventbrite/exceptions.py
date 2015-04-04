# -*- coding: utf-8 -*-
from google.appengine.api import urlfetch_errors


class EventbriteException(Exception):
    pass


class IllegalHttpMethod(EventbriteException):
    pass


class InvalidResourcePath(EventbriteException):
    pass


class UnknownEndpoint(EventbriteException):
    pass


class UnsupportedEndpoint(EventbriteException):
    pass


class InternetConnectionError(urlfetch_errors.Error):
    """
    Wraps urlfetch_errors.Error in order to provide a more
    intuitively named exception.
    """
    pass


class InvalidWebhook(EventbriteException):
    pass
