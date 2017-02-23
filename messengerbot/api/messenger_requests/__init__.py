from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_start_request import MessengerStartRequest



EVENT_TYPE_TO_CLASS = {
	# EventType.MESSAGE: MessengerMessageRequest,
	EventType.START: MessengerStartRequest,
}


def create_request(request_dict):
	if 'event' not in request_dict:
		raise Exception("request is missing field 'event'")

	if request_dict['event'] not in EVENT_TYPE_TO_CLASS:
		raise Exception("event type '{0}' is not supported".format(request_dict['event']))

	return EVENT_TYPE_TO_CLASS[request_dict['event']]().from_dict(request_dict)


__all__ = ['MessengerStartRequest', 'MessengerMessageRequest']


