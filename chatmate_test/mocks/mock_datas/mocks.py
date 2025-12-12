import chatmate_test.mocks.mock_datas.get_chats_response as get_chats_response
import chatmate_test.mocks.mock_datas.get_history_response as get_history_response
from chatmate_utils import get_json_response


class StubVkDateApi:
    def get_history(self, user_id):
        return get_json_response(get_history_response.response)

    def get_chats(self):
        return get_json_response(get_chats_response.response)


class SpyVkDateApi:
    def __init__(self):
        self.last_sended_message = None

    def send_message(self, message):
        self.last_sended_message = message
