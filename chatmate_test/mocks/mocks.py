chats = [
    {
        'id': 1, 'name': 'вика',
        'messages': [
            {
                'text': 'привет, я вика',
                'date': '2025-01-27T16:14:21.211Z',
                'user': 'girl'
            }
        ]
    },
    {
        'id': 2, 'name': 'катя',
        "messages": [
            {
                'text': 'привет, я катя',
                'date': '2025-01-27T16:14:21.211Z',
                'user': 'girl'
            },
        ]
    },
]

class SpyFlirter():
    def guess_next_message(self, chat):
        self.last_messages = chat['messages']
        return "привет как дела?"

    def guess_next_message_options(self, chat):
        return ['опция1', 'опция2']

    def get_last_sended_chat(self):
        msgs = []

        for msg in self.last_messages:
            msg_str = f"{msg['user']}: {msg['text']}"
            msgs.append(msg_str)

        return msgs

class SpyFlirtPlatform:
    def __init__(self):
        self.requests = []
        self.sended_messages = []
        self.chats = []

    def send_message(self, message):
        str_msg = f'{message["user_id"]} {message["text"]}'
        self.sended_messages.append(str_msg)

    def get_chats(self):
        r = f'get_chats()'
        self.requests.append(r)

        return self.chats

    def get_chats_info(self):
        r = f'get_chats_info()'
        self.requests.append(r)

        return [
            {
                'id': 1,
                'name': 'Анна',
                'avatar_url':'avatar_url',
                'last_message_timedelta': {'days': 137, 'hours': 23, 'minutes': 43},
                'is_answered': True,
            }
        ]

class SpyChatRepository:
    def __init__(self):
        self.is_save_called = False

    def save(self, chat):
        self.is_save_called = True

    def find_chat(self, user_id):
        self.is_find_chat_called = True

