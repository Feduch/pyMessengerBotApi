
class MessengerRequest:
    def __init__(self, event_type=None):
        self._event_type = event_type
        self._sender_id = None
        self._recipient_id = None
        self._timestamp = None

    def from_dict(self, request_dict):
        self._sender_id = request_dict['sender']['id']
        self._recipient_id = request_dict['recipient']['id']
        self._timestamp = request_dict['timestamp']
        return self

    @property
    def event_type(self):
        return self._event_type

    @property
    def sender(self):
        return self._sender

    @property
    def recipient(self):
        return self._recipient

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
