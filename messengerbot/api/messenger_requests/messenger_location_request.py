from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerLocationRequest(MessengerRequest):
    def __init__(self):
        super(MessengerLocationRequest, self).__init__(EventType.LOCATION)
        self._lat = None
        self._long = None

    def from_dict(self, request_dict):
        super(MessengerLocationRequest, self).from_dict(request_dict)
        print('MessengerLocationRequest-----------> {0}'.format(request_dict))
        self._lat = request_dict['lat']
        self._long = request_dict['long']
        return self

    @property
    def lat(self):
        return self._lat

    @property
    def long(self):
        return self._long

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)