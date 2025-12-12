import pytest

from chatmate_details.chatmates.chatgpt.chatgpt_assistant import ChatGptAssistant
from chatmate_details.chatmates.chatgpt.browser_chatgpt import BrowserChatgpt



class TestChatgptAssistant:
    def test_generate_message(self):
        browser_chatgpt = BrowserChatgpt()
        assistant = ChatGptAssistant()
        assistant.browser_chatgpt = browser_chatgpt
        msg_user = {'text': 'Привет!', 'is_my': False, 'name': 'Вика'}
        msg_bot = {'text': 'Как дела?', 'is_my': True, 'name': 'Андрей'}
        chat = {'id': 1, 'msgs': [msg_user, msg_bot]}

        msg = assistant.generate_message(chat)

        print(msg)
        assert msg != ""

    @pytest.mark.skip
    def test_generate_message__by_big_chat(self):
        browser_chatgpt = BrowserChatgpt()
        assistant = ChatGptAssistant()
        assistant.browser_chatgpt = browser_chatgpt
        msgs = []
        for i in range(1, 20+1):
            msgs.append({
                "text": f"Привет как дела ({i})",
                "is_my": (i % 2 == 0),
                "name": "Андрей" if i % 2 == 0 else "Вика"
            })
        chat = {'id': 1, 'msgs': msgs}

        for i in range(5+1):
            msg = assistant.generate_message(chat)

            print(i)
            print(msg)
            assert msg != ""