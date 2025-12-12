class SpyBrowserChatgpt:
    def __init__(self):
        self.events = []

    def ask_question(self, chat_name, text):
        event = f'ask_question {chat_name}->{text}'
        self.events.append(event)