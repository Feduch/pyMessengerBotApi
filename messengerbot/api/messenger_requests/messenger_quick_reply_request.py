from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerQuickReplyRequest(MessengerRequest):
    def __init__(self):
        super(MessengerQuickReplyRequest, self).__init__(EventType.QUICK_REPLY)
        self._mid = None
        self._text = None
        self._seq = None
        self._quick_reply = None

    def from_dict(self, request_dict):
        super(MessengerQuickReplyRequest, self).from_dict(request_dict)
        self._mid = request_dict['message']['mid']
        self._text = request_dict['message']['text']
        self._seq = request_dict['message']['seq']
        self._quick_reply = request_dict['message']['quick_reply']['payload']
        return self

    @property
    def quick_reply(self):
        return self._quick_reply

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)