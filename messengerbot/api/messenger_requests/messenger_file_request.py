from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerFileRequest(MessengerRequest):
    def __init__(self):
        super(MessengerFileRequest, self).__init__(EventType.FILE)
        self._mid = None
        self._url = None
        self._type = None
        self._seq = None

    def from_dict(self, request_dict):
        super(MessengerFileRequest, self).from_dict(request_dict)
        self._mid = request_dict['message']['mid']
        self._seq = request_dict['message']['seq']
        attachments = request_dict['message'].get('attachments')
        for attachment in attachments:
            self._payload = attachment['payload']
            self._type = attachment['type']
        return self

    @property
    def url(self):
        return self._url

    @property
    def type(self):
        return self._type

    @property
    def mid(self):
        return self._mid

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)