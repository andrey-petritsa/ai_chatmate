import json
from pathlib import Path

import pytest

from chatmate_details.chatmates.deepseek.deepseek_api import DeepseekApi
from chatmate_utils.env import Env


class TestDeepseekApi:
    HAND_MODE_PROMT = Path("settings/chatmate_promt.txt").read_text(encoding="utf-8")
    DEEPSEEK_TOKEN = Env.load("DEEPSEEK_TOKEN")

    def test_get_chat_response(self):
        api = DeepseekApi(self.DEEPSEEK_TOKEN)
        messages = [
            {"role": "user", "content": "Привет!"},
            {"role": "assistant", "content": "Привет! Как дела?"},
            {"role": "user", "content": "Все хорошо, а у тебя?"}
        ]
        response = api.get_chat_response(messages)

        assert response.status_code == 200

    @pytest.mark.skip("")
    def test_get_chat_response_as_json(self):
        api = DeepseekApi(self.DEEPSEEK_TOKEN)
        messages = [
            {"role": "system", "content": self.HAND_MODE_PROMT},
            {"role": "user", "content": "Привет!"},
            {"role": "assistant", "content": "Привет! Как дела?"},
            {"role": "user", "content": "Все хорошо, а у тебя?"}
        ]
        response = api.get_chat_response(messages)
        text = get_text_from(response)

        assert response.status_code == 200
        assert is_json(text) == True

def is_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False

def get_text_from(response):
    response = response.json()
    text = response['choices'][0]['message']['content']
    return text
