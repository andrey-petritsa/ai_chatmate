from copy import deepcopy


class SendMessageCommand:
    def __init__(self, platform=None, assistant=None):
        self.platform = platform
        self.assistant = assistant

    def execute(self, chat, text=None):
        chat = deepcopy(chat)

        if text == None:
            text = self.assistant.generate_message(chat)

        sent_msg = self.platform.send_message(chat['id'], text)
        chat['msgs'].append(sent_msg)
        return chat