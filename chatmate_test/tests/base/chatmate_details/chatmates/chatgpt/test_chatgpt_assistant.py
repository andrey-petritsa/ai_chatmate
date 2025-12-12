from chatmate_details.chatmates.chatgpt.chatgpt_assistant import ChatGptAssistant
from mocks.spy_browser_chatgpt import SpyBrowserChatgpt


class TestChatgptAssistant:
    def test_generate_message(self):
        spy_browser_chatgpt = SpyBrowserChatgpt()
        assistant = ChatGptAssistant()
        assistant.browser_chatgpt = spy_browser_chatgpt
        msg_user = {'text': 'Привет!', 'is_my': False, 'name': 'Вика'}
        msg_bot = {'text': 'Как дела?', 'is_my': True, 'name': 'Андрей'}
        chat = {'id': 1, 'msgs': [msg_user, msg_bot]}

        assistant.generate_message(chat)

        e_messages = ['(-) Вика: Привет!', '(+) Андрей: Как дела?']

        e_message = '\n'.join(e_messages)
        assert f'ask_question Дайвинчик => {e_message}', spy_browser_chatgpt.events

    def test_generate_message__with_empty_chat(self):
        spy_browser_chatgpt = SpyBrowserChatgpt()
        assistant = ChatGptAssistant()
        assistant.browser_chatgpt = spy_browser_chatgpt
        chat = {'id': 1, 'msgs': []}

        assistant.generate_message(chat)

        assert f'ask_question Дайвинчик => В чате пока что не было сообщений', spy_browser_chatgpt.events