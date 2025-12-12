class ChatPresenter:
    def to_view_chat(self, chat):
        self.__chat = chat
        view_messages = []
        for message in chat['messages']:
            view_messages.append(self.__to_view_messages(message))
        chat['messages'] = view_messages
        return chat

    def __to_view_messages(self, message):
        if message['name'] == 'bot':
            name = 'bot'
            position = 'left'
        else:
            name = self.__chat['name']
            position = 'right'
        msg = {'name':name, 'text':message['text'], 'position':position}
        return msg

    def to_view_chat_info(self, chat_info):
        if chat_info['is_answered']:
            is_answered_status_icon = '👀'
        else:
            is_answered_status_icon = '🙈'

        return {
            'id': chat_info['id'],
            'name': chat_info['name'],
            'avatar_url':chat_info['avatar_url'],
            'last_message_hint':self.__to_str_time_delta(chat_info['last_message_timedelta']),
            'is_answered_status_icon': is_answered_status_icon,
        }
    
    def __to_str_time_delta(self, timedelta):
        if timedelta['days'] > 0:
            return f"{timedelta['days']} дней"
        if timedelta['hours'] > 0:
            return f"{timedelta['hours']} час"
        return f"{timedelta['minutes']} минут"
