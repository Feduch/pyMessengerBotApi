import requests
from requests import RequestException
import traceback
import json


class ApiRequestSender:
    def __init__(self, logger, messenger_bot_api_url, bot_configuration, messenger_bot_user_agent):
        self._logger = logger
        self._messenger_bot_api_url = messenger_bot_api_url
        self._bot_configuration = bot_configuration
        self._user_agent = messenger_bot_user_agent

    def post_request(self, endpoint, payload):
        try:
            headers = requests.utils.default_headers()
            headers.update({
                'User-Agent': self._user_agent
            })
            response = requests.post(self._messenger_bot_api_url + '/' + endpoint, data=payload, headers=headers)
            response.raise_for_status()
            return json.loads(response.text)
        except RequestException as e:
            self._logger.error(u"failed to post request to endpoint={0}, with payload={1}. error is: {2}"
                               .format(endpoint, payload, traceback.format_exc()))
            raise e
        except Exception as ex:
            self._logger.error(u"unexpected Exception while trying to post request. error is: {0}"
                                   .format(traceback.format_exc()))
            raise ex

    def get_request(self, endpoint, payload):
        try:
            response = requests.get(self._messenger_bot_api_url + '/' + endpoint, data=payload)
            response.raise_for_status()
            return json.loads(response.text)
        except RequestException as e:
            self._logger.error(u"failed to post request to endpoint={0}, with payload={1}. error is: {2}"
                               .format(endpoint, payload, traceback.format_exc()))
            raise e
        except Exception as ex:
            self._logger.error(u"unexpected Exception while trying to post request. error is: {0}"
                               .format(traceback.format_exc()))
            raise ex

    def get_user_profile(self, user_id):
        if user_id is None:
            raise Exception("missing parameter id")

        payload = {
            'access_token': self._bot_configuration.access_token,
            'fields': 'first_name,last_name,profile_pic,locale,timezone,gender'
        }
        result = self.get_request(
            endpoint=user_id,
            payload=json.dumps(payload))

        if not result['error'] == 0:
            raise Exception(u"failed with status: {0}, message: {1}"
                            .format(result['error']['code'], result['error']['message']))

        return result