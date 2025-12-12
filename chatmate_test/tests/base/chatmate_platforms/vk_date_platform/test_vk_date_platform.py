
import pytest

from chatmate_test.mocks.mock_datas.mocks import StubVkDateApi, SpyVkDateApi
from chatmate_test.utils.chat_utils import to_str_one
from mocks.stub_time_provider import StubTimeProvider
from chatmate_platforms.vk.vk_platform import VkDatePlatform


@pytest.mark.skip("")
class TestVkDatePlatform:
    def setup_method(self):
        self.e_avatar_url = 'https://sun9-west.userapi.com/sun9-62/s/v1/if2/1VPr6H_XuMyMUBIGgKXueFg4vXsbD0BnBqVTTO_24oxioDhU368Q_nx9_oDaXSWPbA0GWNBYjjAj1_4d0k77U2d2iLyiOw.jpg?quality=90&size=108x192'

    def test_send_message(self):
        spy = SpyVkDateApi()
        platform = VkDatePlatform(spy)

        msg = {'user_id': 1, 'text': 'привет как дела?'}
        platform.send_message(msg)

        assert 'привет как дела?' == spy.last_sended_message['text']

    def test_get_chats(self):
        platform = VkDatePlatform(StubVkDateApi())
        chats = platform.get_chats()

        assert to_str_one(chats[0]) == 39277097

    def test_get_chat(self):
        platform = VkDatePlatform(StubVkDateApi())
        user_id = 1
        chat = platform.get_chat(user_id)

        assert to_str_one(chat) == 1



    def test_get_chats_info(self):
        platform = VkDatePlatform(StubVkDateApi())
        #utils.time_provider = StubTimeProvider()
        #utils.time_provider.now_date = '2025-06-25T12:00:00.211Z'
        chats_info = platform.get_chats_info()

        e_chats_info = [
            {
                'id': 39277097,
                'name': 'Мариам',
                'avatar_url':self.e_avatar_url,
                'last_message_timedelta': {'days': 137, 'hours': 23, 'minutes': 43},
                'is_answered': True,
            }
        ]
        assert chats_info == e_chats_info
