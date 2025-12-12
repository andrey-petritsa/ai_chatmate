from chatmate_details.telegram.client.telegram_api import TelegramApi
from chatmate_details.telegram.client.message_parser import MessageParser



class TelegramMessenger:
    def __init__(self):
        self.tg_api = TelegramApi()
        self.message_parser = MessageParser()

    def get_chat(self, chat_id):
        api_msgs = self.tg_api.fetch_all(chat_id)
        msgs = [self.message_parser.to_msg(api_msg) for api_msg in api_msgs]
        chat = {'id': chat_id, 'msgs': msgs}
        return chat

    def get_chat_slice(self, chat_id, count):
        api_msgs = self.tg_api.fetch_latest_count(chat_id, count)
        msgs = [self.message_parser.to_msg(api_msg) for api_msg in api_msgs]
        chat = {'id': chat_id, 'msgs': msgs}
        return chat

    def send_message(self, chat_id, msg):
        sent_msg = self.tg_api.send_message(chat_id, msg)
        return self.message_parser.to_msg(sent_msg)

    def get_available_chats(self):
        dialogs = self.tg_api.app.get_dialogs()
        return list(dialogs)
