import pytest

from chatmate_details.telegram.client.telegram_messenger import TelegramMessenger


class TestTelegramMessenger:
    def test_get_chat(self):
        messenger = TelegramMessenger()
        chat = messenger.get_chat(chat_id='@leomatchbot')
        assert chat is not None

    #@pytest.mark.skip()
    def test_send_message(self):
        messenger = TelegramMessenger()
        sent_msg = messenger.send_message('@acrosspaper', 'hello')
        assert sent_msg is not None

    def test_get_available_chats(self):
        messenger = TelegramMessenger()
        chats = messenger.get_available_chats()
        print(chats)
        assert chats is not None
