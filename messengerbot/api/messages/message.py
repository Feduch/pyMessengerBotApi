from abc import abstractmethod


class Message:
    def __init__(self, recipient_id):
        self._recipient_id = recipient_id

    @abstractmethod
    def to_dict(self):
        message_data = {}
        if self._recipient_id:
            message_data['recipient']['id'] = self._recipient_id
        return message_data

    @abstractmethod
    def from_dict(self, message_data):
        if 'recipient' in message_data:
            self._recipient_id = message_data['recipient']['id']
        return self

    @property
    def recipient_id(self):
        return self._recipient_id

    @abstractmethod
    def validate(self):
        pass

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
