class BotConfiguration(object):
	def __init__(self, access_token, name=None):
		self._access_token = access_token
		self._name = name

	@property
	def name(self):
		return self._name

	@property
	def auth_token(self):
		return self._access_token
