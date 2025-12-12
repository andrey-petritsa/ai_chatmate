import pytest

from chatmate_platforms.vk.vk_api import VkDateApi
from chatmate_platforms.vk.vk_date_token_extractor import VkDateTokenExtractor

@pytest.mark.skip("")
class TestVkDateApi:
    def setup_method(self):
        self.user_id = None
        self.api = VkDateApi()
        self.api.token = VkDateTokenExtractor.extract()

    @pytest.mark.integration
    def test_get_history(self):
        response = self.api.get_history(self.user_id)
        assert response.ok is True

    @pytest.mark.integration
    def test_send_message(self):
        message_text = 'тест'
        message = {'user_id': self.user_id, 'text': message_text}
        response = self.api.send_message(message)
        assert response.ok is True

    @pytest.mark.integration
    def test_get_chats(self):
        response = self.api.get_chats()
        assert response.ok is True
