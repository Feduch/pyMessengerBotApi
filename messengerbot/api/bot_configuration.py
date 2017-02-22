class BotConfiguration:
	def __init__(self, access_token, verify_token, name=None):
		self._access_token = access_token
		self._name = name
		self._verify_token = verify_token

	@property
	def name(self):
		return self._name

	@property
	def access_token(self):
		return self._access_token

	@property
	def verify_token(self):
		return self._verify_token
