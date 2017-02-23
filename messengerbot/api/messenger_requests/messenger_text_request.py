from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerTextRequest(MessengerRequest):
    def __init__(self):
        super(MessengerTextRequest, self).__init__(EventType.TEXT)
        self._mid = None
        self._text = None
        self._seq = None

    def from_dict(self, request_dict):
        super(MessengerTextRequest, self).from_dict(request_dict)
        self._mid = request_dict['message']['mid']
        self._text = request_dict['message']['text']
        self._seq = request_dict['message']['seq']
        return self

    @property
    def text(self):
        return self._text

    @property
    def mid(self):
        return self._mid

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)