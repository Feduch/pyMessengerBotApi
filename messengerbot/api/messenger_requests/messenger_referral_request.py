from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_request import MessengerRequest


class MessengerReferralRequest(MessengerRequest):
    def __init__(self):
        super(MessengerReferralRequest, self).__init__(EventType.REFERRAL)
        self._ref = None
        self._type = None
        self._source = None

    def from_dict(self, request_dict):
        super(MessengerReferralRequest, self).from_dict(request_dict)
        self._ref = request_dict['referral']['ref']
        self._type = request_dict['referral']['type']
        self._source = request_dict['referral']['source']
        return self

    @property
    def ref(self):
        return self._ref

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)