from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerPostbackRequest(MessengerRequest):
    def __init__(self):
        super(MessengerPostbackRequest, self).__init__(EventType.POSTBACK)
        self._payload = None

    def from_dict(self, request_dict):
        super(MessengerPostbackRequest, self).from_dict(request_dict)
        self._payload = request_dict['postback']['payload']
        return self

    @property
    def payload(self):
        return self._payload

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)