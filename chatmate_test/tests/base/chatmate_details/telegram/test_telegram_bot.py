from chatmate_details.telegram.bot.telegram_bot_api import TelegramBotApi
from chatmate_utils.env import Env


class TestTelegramBot:
    def test_get_updates(self):
        token = Env.load('TG_BOT_TOKEN')
        telegram = TelegramBotApi(token)
        response = telegram.get_updates()
        
        assert response != None

    def test_send_message(self):
        chat_id = Env.load('TG_BOT_CHAT_ID')
        token = Env.load('TG_BOT_TOKEN')
        telegram = TelegramBotApi(token)
        response = telegram.send_message(chat_id, "test")

        assert response != None

    def test_get_messages(self):
        chat_id = Env.load('TG_BOT_CHAT_ID')
        token = Env.load('TG_BOT_TOKEN')
        telegram = TelegramBotApi(token)
        msgs = telegram.get_messages(chat_id)

        assert msgs != []