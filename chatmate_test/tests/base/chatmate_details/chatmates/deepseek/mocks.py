from chatmate_utils import get_json_response


class SpyDeepseekApi:
    def get_chat_response(self, messages):
        self.last_messages = messages
        return get_json_response({})