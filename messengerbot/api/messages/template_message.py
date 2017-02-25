from messengerbot.api.messages.message import Message


class TemplateMessage(Message):
    def __init__(self, type='template', text=None, buttons=None, elements=None):
        self._text = text
        self._buttons = buttons
        self._elements = elements
        self._type = type
        self._template_type = 'button'
        if elements is None:
            self._template_type = 'generic'

    def to_dict(self):
        message_data = super(TemplateMessage, self).to_dict()
        message_data['attachment'] = {}
        message_data['attachment']['payload'] = {}
        message_data['attachment']['type'] = self._type
        message_data['attachment']['payload']['template_type'] = self._template_type
        if self._template_type=="button":
            message_data['attachment']['payload']['text'] = self._text
            message_data['attachment']['payload']['buttons'] = self._buttons
        if self._template_type == "generic":
            message_data['attachment']['payload']['elements'] = []
            message_data['attachment']['payload']['elements'] = self._elements
            message_data['attachment']['payload']['elements']['buttons'] = self._buttons
        return message_data

    def from_dict(self, message_data):
        super(TemplateMessage, self).from_dict(message_data)
        if 'text' in message_data['attachment']['payload']:
            self._text = message_data['attachment']['payload']
        if 'buttons' in message_data['attachment']['payload']['buttons']:
            self._buttons = message_data['attachment']['payload']['buttons']
        return self

    def validate(self):
        return self._text is not None

    @property
    def text(self):
        return self._text

    @property
    def buttons(self):
        return self._buttons

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
