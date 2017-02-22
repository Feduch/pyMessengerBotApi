from ..version import __version__

DEFAULT_API_VERSION = 2.8
MESSENGER_BOT_API_URL = 'https://graph.facebook.com/v{0}'.format(DEFAULT_API_VERSION)
MESSENGER_BOT_USER_AGENT = "MessengerBot-Python/" + __version__


class BOT_API_ENDPOINT:
	SEND_MESSAGE = '/me/messages'