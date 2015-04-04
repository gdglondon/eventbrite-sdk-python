import functools

from google.appengine.api import urlfetch_errors

from .exceptions import InternetConnectionError
from .models import EventbriteObject


def objectify(func):
    """ Converts the returned value from a models.Payload to
        a models.EventbriteObject. Used by the access methods
        of the client.Eventbrite object
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            url, payload = func(*args, **kwargs)
        except urlfetch_errors.Error as e:
            raise InternetConnectionError(e)
        return EventbriteObject.create(url, payload)
    return wrapper

