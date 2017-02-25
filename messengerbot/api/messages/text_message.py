from messengerbot.api.messages.message import Message


class TextMessage(Message):
    def __init__(self, recipient_id, text=None):
        super(TextMessage, self).__init__(recipient_id)
        self._text = text

    def to_dict(self):
        message_data = super(TextMessage, self).to_dict()
        message_data['text'] = self._text
        return message_data

    def from_dict(self, message_data):
        super(TextMessage, self).from_dict(message_data)
        if 'text' in message_data:
            self._text = message_data['text']
        return self

    def validate(self):
        return self._text is not None

    @property
    def text(self):
        return self._text

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
