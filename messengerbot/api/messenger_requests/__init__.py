from messengerbot.api.messenger_requests.messenger_start_request import MessengerStartRequest
from messengerbot.api.messenger_requests.messenger_postback_request import MessengerPostbackRequest
from messengerbot.api.messenger_requests.messenger_referral_request import MessengerReferralRequest
from messengerbot.api.messenger_requests.messenger_quick_reply_request import MessengerQuickReplyRequest
from messengerbot.api.messenger_requests.messenger_text_request import MessengerTextRequest
from messengerbot.api.messenger_requests.messenger_file_request import MessengerFileRequest
from messengerbot.api.messenger_requests.messenger_location_request import MessengerLocationRequest


def create_request(request_dict):
    for event in request_dict['entry']:
        if event.get('messaging'):
            messaging = event['messaging']
            for data in messaging:
                if data.get('postback'):
                    if data['postback'].get('referral'):
                        return MessengerStartRequest().from_dict(data)
                    else:
                        return MessengerPostbackRequest().from_dict(data)
                if data.get('referral'):
                    return MessengerReferralRequest().from_dict(data)
                if data.get('message'):
                    if data['message'].get('quick_reply'):
                        return MessengerQuickReplyRequest().from_dict(data)
                    elif data['message'].get('attachments'):
                        attachments = data['message'].get('attachments')
                        for attachment in attachments:
                            if attachment['type']=='location':
                                # Данные о своем местонахождении
                                return MessengerLocationRequest().from_dict(data)
                            else:
                                return MessengerFileRequest().from_dict(data)
                    else:
                        return MessengerTextRequest().from_dict(data)