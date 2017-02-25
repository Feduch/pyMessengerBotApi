from abc import abstractmethod


class Message:
    def __init__(self):
        pass

    @abstractmethod
    def to_dict(self):
        message_data = {}
        message_data['message'] = {}
        return message_data

    @abstractmethod
    def from_dict(self, message_data):
        return self

    @abstractmethod
    def validate(self):
        pass

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
