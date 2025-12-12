class ChatPresenter:
    def present(self, chat):
        chat_messages = []
        for message in chat:
            chat_messages.append(self.__to_str_message(message))
        return "\n\n".join(chat_messages)

    def __to_str_message(self, message):
        msg = f"{message['name']}: {message['text']}"
        if message['position'] == 'right':
            msg = "❤️" + msg
        else:
            msg = "🤖" + msg
        return msg