import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from chatmate_platforms.vk.exception import InvalidTokenException


class VkDateApi:
    def __init__(self):
        self.token = None

    def get_history(self, user_id):
        url = "https://dating.vk.com/api/messenger.getHistory"
        request = self.make_get_history_request(user_id)
        headers = {"content-type": request.content_type}

        response = requests.post(url, headers=headers, data=request)
        if not response.ok:
            response_content = response.json()
            if response_content['error'] == 'token_invalid':
                raise InvalidTokenException()
            raise Exception(response.text + f" user_id: {user_id}")

        return response

    def make_get_history_request(self, user_id):
        fields = {
            "user_id": str(user_id),
            "limit": "25",
            "offset": "0",
            "_token":self.token,
            "_agent": "love1 version:1.1.0 build:42 commit:86f7253249 env:production platform:desktop_web client:0.0/web/none lang:ru tz:10800 vkid:179377912 screen:d/795x709/1.100000023841858",
            "_session": "179377912_1739035613555",
            "_v": "1.13",
        }

        return MultipartEncoder(
            fields=fields,
            boundary="----WebKitFormBoundary1R9RTgZGf7Cm5KWr"
        )


    def send_message(self, message):
        r = self.__make_send_message_request(message)
        return self.__send_send_message_request(r)

    def __make_send_message_request(self, message):
        fields = {
            "user_id": str(message['user_id']),
            "text": message['text'],
            "_token": self.token,
            "_v": "1.13",
        }

        return {
            'url':"https://dating.vk.com/api/messenger.send",
            'headers':{"content-type":MultipartEncoder(fields=fields, boundary="----WebKitFormBoundaryVCgv4x0LhAoyptwt").content_type},
            'data':MultipartEncoder(fields=fields, boundary="----WebKitFormBoundaryVCgv4x0LhAoyptwt")
        }

    def __send_send_message_request(self, r):
        response = requests.post(r['url'], headers=r['headers'], data=r['data'])
        if not response.ok:
            response_content = response.json()
            if response_content['error'] == 'token_invalid':
                raise InvalidTokenException()
            raise Exception(response.text + str(response.status_code))
        return response

    def get_chats(self):
        url = "https://dating.vk.com/api/messenger.getChats"
        request = self.make_get_chats_request()
        headers = {"content-type": request.content_type}
        response = requests.post(url, headers=headers, data=request)
        if not response.ok:
            response_content = response.json()
            if response_content['error'] == 'token_invalid':
                raise InvalidTokenException()
            raise Exception(response.text)

        return response

    def make_get_chats_request(self):
        fields = {
            "limit": "24",
            "offset": "0",
            "filter": "chat",
            "_token": self.token,
            "_agent": "love1 version:1.1.0 build:45 commit:b56925d360 env:production platform:desktop_web client:0.0/web/none lang:ru tz:10800 vkid:179377912 screen:d/795x709/1.100000023841858",
            "_session": "179377912_1740251026686",
            "_v": "1.13",
        }

        return MultipartEncoder(
            fields=fields,
            boundary="----WebKitFormBoundary8fenChiD4DILfGM4"
        )
