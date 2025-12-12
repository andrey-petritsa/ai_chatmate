from chatmate_platforms.telegram.telegramplatform import TelegramPlatform
from mocks.spy_messanger import SpyMessanger
from mocks.testable_daivinchik import TestableTelegramPlatform


class TestTelegramPlatform:
    def test_send_message(self):
        messanger = SpyMessanger()
        platform = TelegramPlatform(messanger)
        platform.send_message(chant_id=1, text="привет")

        assert "send_message 1->привет" in messanger.events

    def test_get_chats(self):
        messanger = SpyMessanger()
        platform = TestableTelegramPlatform(messanger)
        text_link_entity = {'type': 'text_link', 'url': 'https://t.me/test?text=123'}
        platform.msgs = [
            {'text': 'Начинай общаться', 'entities': [text_link_entity]},
            {'text': '2', 'entities': []}
        ]
        chats = platform.get_chats()

        assert chats[0]['id'] == '@test'
        assert len(chats) != 0

    def test_can_like(self):
        messanger = SpyMessanger()
        platform = TestableTelegramPlatform(messanger)
        platform.msgs = [
            {'text': '', 'photo': {'caption': 'Лена, Курск', 'file_id': '1'}}
        ]
        assert True == platform.can_like()

    def test_like_next_person(self):
        messanger = SpyMessanger()
        platform = TestableTelegramPlatform(messanger)
        platform.msgs = [
            {'text': '', 'photo': {'caption': 'Лена, Курск', 'file_id': '1'}}
        ]

        platform.like_next()

        assert 'send_message @leomatchbot->❤️' in messanger.events

    def test_get_chat_links(self):
        messanger = SpyMessanger()
        platform = TestableTelegramPlatform(messanger)
        text_link_entity = {'type': 'text_link', 'url': 'https://t.me/test?text=123'}
        platform.msgs = [
            {'text': 'Начинай общаться', 'entities': [text_link_entity]},
            {'text': '2', 'entities': []}
        ]
        links = platform.get_chat_links()

        assert links == ['@test']

    def test_get_chat_msgs(self):
        messanger = SpyMessanger()
        platform = TestableTelegramPlatform(messanger)
        text_link_entity = {'type': 'text_link', 'url': 'https://t.me/test?text=123'}
        platform.msgs = [
            {'text': 'Начинай общаться', 'entities': [text_link_entity]},
            {'text': '2', 'entities': []}
        ]
        msgs = platform.get_chat_msgs('@test')

        assert msgs == [{'message': 'привет', 'is_my':False, 'name': 'персона 123'}]
