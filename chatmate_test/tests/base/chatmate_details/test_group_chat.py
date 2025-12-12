from mocks.stub_time_provider import StubTimeProvider
from chatmate_details.telegram.bot.telegrambot import TelegramBot


class SpyTelegram:
    def send_message(self, text, group_id):
        self.last_sended_message = f"{text} to {group_id}"

    def get_updates(self, update_id=None):
        self.last_called_method = f"get_updates since update_id {update_id}"

        return {
            "ok": True,
            "result": [
                {
                    "update_id": 1,
                    "message": {
                        "message_id": 17,
                        "from": {
                            "id": 1,
                            "is_bot": False,
                            "first_name": "Андрей",
                            "last_name": "Петрица",
                            "username": "Acrosspaper",
                            "language_code": "ru",
                            "is_premium": True
                        },
                        "chat": {
                            "id": -1,
                            "title": "Конор",
                            "type": "group",
                            "all_members_are_administrators": True,
                            "accepted_gift_types": {
                                "unlimited_gifts": False,
                                "limited_gifts": False,
                                "unique_gifts": False,
                                "premium_subscription": False
                            }
                        },
                        "date": 1,
                        "text": "старое сообщение"
                    }
                },

                {
                    "update_id": 2,
                    "message": {
                        "message_id": 17,
                        "from": {
                            "id": 1,
                            "is_bot": False,
                            "first_name": "Андрей",
                            "last_name": "Петрица",
                            "username": "Acrosspaper",
                            "language_code": "ru",
                            "is_premium": True
                        },
                        "chat": {
                            "id": -1,
                            "title": "Конор",
                            "type": "group",
                            "all_members_are_administrators": True,
                            "accepted_gift_types": {
                                "unlimited_gifts": False,
                                "limited_gifts": False,
                                "unique_gifts": False,
                                "premium_subscription": False
                            }
                        },
                        "date": 2,
                        "text": "тест"
                    }
                }
            ]
        }

class TestGroupChat:
    def setup_method(self):
        self.telegram = SpyTelegram()
        self.chat = TelegramBot(self.telegram)
        self.chat.time_provider = StubTimeProvider()

    def test_send_message(self):
        self.chat.send_message('abracadabra', 1)
        assert self.telegram.last_sended_message == 'abracadabra to 1'

    def test_get_messages(self):
        self.chat.time_provider.now_date_timestamp = 2
        e_message = {'id':1, 'first_name': 'Андрей', 'last_name': 'Петрица', 'date': 2, 'text': 'тест'}
        timestamp = 2
        messages = self.chat.get_messages_since(timestamp)
        assert e_message == messages[0]

        self.chat.get_messages_since(timestamp)
        assert self.telegram.last_called_method == "get_updates since update_id 3"