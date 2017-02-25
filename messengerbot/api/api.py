import json
import logging

from .consts import MESSENGER_BOT_API_URL, MESSENGER_BOT_USER_AGENT
from messengerbot.api.messenger_requests import create_request
from messengerbot.api.api_request_sender import ApiRequestSender
from messengerbot.api.message_sender import MessageSender


class Api:
    def __init__(self, bot_configuration):
        self._logger = logging.getLogger('messenger.bot.api')
        self._bot_configuration = bot_configuration
        self._request_sender = ApiRequestSender(self._logger, MESSENGER_BOT_API_URL, bot_configuration,
                                                MESSENGER_BOT_USER_AGENT)
        self._message_sender = MessageSender(self._logger, self._request_sender, bot_configuration)

    @property
    def name(self):
        return self._bot_configuration.name

    @property
    def verify_token(self):
        return self._bot_configuration.verify_token

    def get_user_profile(self, user_id):
        return self._request_sender.get_user_profile(user_id)

    def parse_request(self, request_data):
        self._logger.debug(u"parsing request={0}".format(request_data))
        request_dict = json.loads(request_data)
        request = create_request(request_dict)
        self._logger.debug(u"parsed request={0}".format(request))
        return request

    def send_message(self, recipient_id, message):
        """
		:param recipient_id: Messenger user id
		:param message_text: text
		:return: list of tokens of the sent messages
		"""
        self._logger.debug("going to send message text: {0}, recipient_id: {1}".format(message, recipient_id))
        if not isinstance(message, str):
            sent_messages_tokens = []

            token = self._message_sender.send_message(recipient_id, message)
            sent_messages_tokens.append(token)

        return sent_messages_tokens