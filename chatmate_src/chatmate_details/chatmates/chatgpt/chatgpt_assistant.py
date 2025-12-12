from chatmate_details.chatmates.msg_stringify import MsgStringify


class ChatGptAssistant:
    def __init__(self):
        self.browser_chatgpt = None

    def generate_message(self, chat):
        if not chat['msgs']:
            return self.browser_chatgpt.ask_question('Дайвинчик', 'В чате пока что не было сообщений')

        str_msgs = [MsgStringify.to_str_msg(msg) for msg in chat['msgs']]
        chat_msgs_str = '\n'.join(str_msgs)
        return self.browser_chatgpt.ask_question('Дайвинчик', chat_msgs_str)

