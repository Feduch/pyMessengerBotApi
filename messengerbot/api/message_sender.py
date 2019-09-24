import json

from messengerbot.api.consts import BOT_API_ENDPOINT


class MessageSender:
    def __init__(self, logger, request_sender, bot_configuration):
        self._logger = logger
        self._request_sender = request_sender
        self._bot_configuration = bot_configuration

    def send_message(self, recipient_id, message):
        if not message.validate():
            self._logger.error(u"failed validating message: {0}".format(message))
            raise Exception("failed validating message: {0}".format(message))

        payload = {"recipient":{"id": recipient_id},"message": message.to_dict()}

        self._logger.debug(u"going to send message: {0}".format(payload))
        result = self._request_sender.post_request(
            BOT_API_ENDPOINT.SEND_MESSAGE,
            json.dumps(payload)
        )

        if 'error' in result:
            raise Exception(u"failed with result: {0}".format(result))

        return result['message_id']