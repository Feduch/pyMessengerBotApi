from setuptools import setup
exec(open('messengerbot/version.py').read())
setup(
	name='messengerbot',
	version=__version__,
	packages=['messengerbot', 'messengerbot.api', 'messengerbot.api.messenger_requests',
			  'messengerbot.api.messages', 'messengerbot.api.messages.data_types'],
	install_requires=['requests'],
	url='https://github.com/Feduch/pyMessengerBotApi',
)
