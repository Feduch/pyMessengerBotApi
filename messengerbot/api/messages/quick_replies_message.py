from messengerbot.api.messages.message import Message


class QuikRepliesMessage(Message):
    def __init__(self, text=None):
        self._text = text

    def to_dict(self):
        message_data = super(QuikRepliesMessage, self).to_dict()
        message_data['message']['text'] = self._text
        return message_data

    def from_dict(self, message_data):
        super(QuikRepliesMessage, self).from_dict(message_data)
        if 'text' in message_data['message']:
            self._text = message_data['message']['text']
        return self

    def validate(self):
        return self._text is not None

    @property
    def text(self):
        return self._text

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
