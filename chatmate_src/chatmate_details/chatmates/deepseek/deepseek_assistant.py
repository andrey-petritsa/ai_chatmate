import json
from pathlib import Path

from chatmate_details.chatmates.deepseek.deepseek_api import DeepseekApi
from chatmate_utils.env import Env
from chatmate_utils.logger import logger


class DeepseekAssistant:
    def __init__(self):
        self.promt = Path("settings/chatmate_promt.txt").read_text(encoding="utf-8")
        self.multi_message_promt = self.__get_multi_message_promt()
        token = Env.load('DEEPSEEK_TOKEN')

        self.deepseek_api = DeepseekApi(token)

    def generate_message(self, chat):
        messages = self.__generate_api_msgs_for_one_msg(chat)
        response = self.deepseek_api.get_chat_response(messages)
        response = response.json()
        return response['choices'][0]['message']['content']

    def generate_messages(self, chat):
        max_attempts = 5
        for attempt in range(max_attempts):
            logger.app_info(f'DeepseekAssistant generate messages for context {len(chat["msgs"])} attempt {attempt}')
            messages = self.__generate_api_msgs_for_multi_msgs(chat)
            response = self.deepseek_api.get_chat_response(messages)
            response = response.json()
            response_text = response['choices'][0]['message']['content']
            lines = [line.strip() for line in response_text.split('\n') if line.strip()]
            if len(lines) >= 1:
                return lines

        raise RuntimeError(
            "Unable to generate a list of non-empty messages from Deepseek after "
            f"{max_attempts} attempts."
        )

    def __generate_api_msgs_for_one_msg(self, chat):
        system_promt = {'role': 'system', 'content': self.promt}
        user_promts = [self.__generate_user_promt(msg) for msg in chat['msgs']]
        return [system_promt] + user_promts

    def __generate_api_msgs_for_multi_msgs(self, chat):
        system_promt = {'role': 'system', 'content': self.multi_message_promt}
        user_promts = [self.__generate_user_promt(msg) for msg in chat['msgs']]
        return [system_promt] + user_promts

    def __generate_user_promt(self, msg) -> dict[str, str]:
        return {'role':'user', 'content':self.__to_str(msg)}

    def __to_str(self, msg):
        return json.dumps(msg, ensure_ascii=False)

    def __get_multi_message_promt(self):
        multi_msg_promt = (
            "Ты должен вернуть 10 вариантов ответов, "
            "Верни их каждый с новой строки."
        )
        return self.promt + '\n' + multi_msg_promt
