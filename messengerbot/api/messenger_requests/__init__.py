from messengerbot.api.event_type import EventType
from messengerbot.api.messenger_requests.messenger_start_request import MessengerStartRequest
from messengerbot.api.messenger_requests.messenger_postback_request import MessengerPostbackRequest
from messengerbot.api.messenger_requests.messenger_referral_request import MessengerReferralRequest
from messengerbot.api.messenger_requests.messenger_quick_reply_request import MessengerQuickReplyRequest
from messengerbot.api.messenger_requests.messenger_text_request import MessengerTextRequest


def create_request(request_dict):
    for event in request_dict['entry']:
        messaging = event['messaging']
        for data in messaging:
            if data.get('postback'):
                if data['postback'].get('referral'):
                    MessengerStartRequest().from_dict(data)
                else:
                    MessengerPostbackRequest().from_dict(data)
            if data.get('referral'):
                MessengerReferralRequest().from_dict(data)
            if data.get('message'):
                if data['message'].get('quick_reply'):
                    MessengerQuickReplyRequest().from_dict(data)
                elif data['message'].get('attachments'):
                    attachments = data['message'].get('attachments')
                    for attachment in attachments:
                        if attachment['type']=='location':
                            # TODO: Данные о своем местонахождении
                            pass
                        else:
                            # TODO: Обработка файлов
                            pass
                else:
                    MessengerTextRequest().from_dict(data)