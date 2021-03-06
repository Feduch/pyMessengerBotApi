from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerStartRequest(MessengerRequest):
    def __init__(self):
        super(MessengerStartRequest, self).__init__(EventType.START)
        self._ref = None
        self._type = None
        self._source = None
        self._payload = None

    def from_dict(self, request_dict):
        super(MessengerStartRequest, self).from_dict(request_dict)
        self._ref = request_dict['postback']['referral']['ref']
        self._type = request_dict['postback']['referral']['type']
        self._source = request_dict['postback']['referral']['source']
        self._payload = request_dict['postback']['payload']
        return self

    @property
    def ref(self):
        return self._ref

    @property
    def payload(self):
        return self._payload

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)