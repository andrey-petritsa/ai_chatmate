from chatmate_details.telegram.bot.telegram_bot_api import TelegramBotApi
from chatmate_utils.env import Env


class TelegramBotVoterPort:
    def __init__(self):
        self.group_id = Env.load('TG_BOT_CHAT_ID')
        self.telegram_bot_api = TelegramBotApi(Env.load('TG_BOT_TOKEN'))

    def send_message(self, text):
        self.telegram_bot_api.send_message(self.group_id, text)

    def get_messages(self):
        api_msgs = self.telegram_bot_api.get_messages(self.group_id)
        msgs = self.__convert_to_msgs(api_msgs)
        return msgs

    def __convert_to_msgs(self, api_msgs):
        msgs = []
        for msg in api_msgs:
            first_name = msg['from'].get('first_name', '---')
            user_id = msg['from'].get('id')
            msgs.append({
                'text':msg['text'],
                'is_my':False,
                'name':first_name,
                'date':msg['date'],
                'sender': {'id': user_id}
            })
        return msgs