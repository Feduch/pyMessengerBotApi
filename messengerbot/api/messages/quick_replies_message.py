from messengerbot.api.messages.message import Message


class QuikRepliesMessage(Message):
    def __init__(self, text=None, buttons=None):
        self._text = text
        self._quick_replies = buttons

    def to_dict(self):
        message_data = super(QuikRepliesMessage, self).to_dict()
        message_data['text'] = self._text
        message_data['quick_replies'] = self._quick_replies
        return message_data

    def from_dict(self, message_data):
        super(QuikRepliesMessage, self).from_dict(message_data)
        if 'text' in message_data:
            self._text = message_data['text']
        if 'quick_replies' in message_data:
            self._quick_replies = message_data['quick_replies']
        return self

    def validate(self):
        return self._text is not None

    @property
    def text(self):
        return self._text

    @property
    def quick_replies(self):
        return self._quick_replies

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
