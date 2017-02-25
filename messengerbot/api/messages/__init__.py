from messengerbot.api.messages.message_type import MessageType
from messengerbot.api.messages.text_message import TextMessage
from messengerbot.api.messages.file_message import FileMessage
from messengerbot.api.messages.quick_replies_message import QuikRepliesMessage
from messengerbot.api.messages.template_message import TemplateMessage

MESSAGE_TYPE_TO_CLASS = {
    MessageType.TEXT: TextMessage,
    MessageType.QUICK_REPLY: QuikRepliesMessage,
    MessageType.FILE: FileMessage,
    MessageType.TEMPLATE: TemplateMessage,
}


def get_message(message_dict):
    if 'type' not in message_dict:
        raise Exception("message data doesn't contain a type")

    if message_dict['type'] not in MESSAGE_TYPE_TO_CLASS:
        raise Exception(u"message type '{0}' is not supported".format(message_dict['type']))

    return MESSAGE_TYPE_TO_CLASS[message_dict['type']]().from_dict(message_dict)


__all__ = ['TextMessage', 'FileMessage', 'QuikRepliesMessage', 'TemplateMessage']
