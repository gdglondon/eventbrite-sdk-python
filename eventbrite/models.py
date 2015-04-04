# -*- coding: utf-8 -*-
import pprint
import json
from .utils import reverse


class EventbriteObject(dict):

    is_list = None
    is_paginated = None
    pagination = None  # pagination dict w/ keys: object_count, page_number, page_size, page_count
    type = ""
    id = None
    pk = None

    @classmethod
    def create(cls, url, response):
        data = json.loads(response.content)
        evbobject = cls(data)
        evbobject.resource_uri = url
        evbobject.ok = (response.status_code == 200)
        evbobject.elapsed = 0
        evbobject.headers = response.headers
        evbobject.reason = 'Unknown'
        evbobject.status_code = response.status_code
        api_data_type = reverse(evbobject.resource_uri)
        # TODO: figure out what to do with endpoint, which doesn't have defined serializer
        # TODO: solve issue with non-standard serializes not mapping directly to defined objects
        evbobject.type = api_data_type.get("serializer", "")
        # if it's paginated, it's a list, otherwise we don't know yet
        if api_data_type.get("response_type") == "paginated_response":
            evbobject.is_list = True #evbobject.is_paginated = True
            evbobject.is_paginated = True
        else:
            evbobject.is_list = False #evbobject.is_paginated = False
            evbobject.is_paginated = False
        evbobject.pk = evbobject.id = data.get('id')
        evbobject.pagination = data.get('pagination')
        return evbobject


    @property
    def pretty(self):
        return pprint.pformat(self)
