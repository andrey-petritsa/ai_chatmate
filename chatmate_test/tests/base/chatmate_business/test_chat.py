from mocks.stub_time_provider import StubTimeProvider
from chatmate_business.chat import Chat


class TestChat:
    def test_is_chat_answered(self):
        chat = Chat()
        msg = {'is_my': True}
        chat_data = {'id': 1, 'msgs': [msg]}

        assert chat.is_answered(chat_data) == True

    def test_should_write(self):
        chat = Chat()
        chat.time_provider = StubTimeProvider()

        msg = {'is_my': False, 'date': 0}
        chat_data = {'id': 1, 'msgs': [msg]}
        assert chat.should_write(chat_data) == True

        chat_data = {'id': 1, 'msgs': []}
        assert chat.should_write(chat_data) == True

        three_hours = 3 * 60 * 60
        chat.time_provider.now_date_timestamp = three_hours
        msg = {'is_my': True, 'date': 0}
        chat_data = {'id': 1, 'msgs': [msg]}
        assert chat.should_write(chat_data) == True