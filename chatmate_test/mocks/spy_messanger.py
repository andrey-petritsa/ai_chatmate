class SpyMessanger:
    def __init__(self):
        self.events = []
        chat = {
            'id': '@test',
            'msgs': [{'message': 'привет', 'is_my':False, 'name': 'персона 123'}]
        }
        self.chats = {
            '@test': chat
        }

    def send_message(self, person_id, message):
        event = f'send_message {person_id}->{message}'
        self.events.append(event)

    def get_chat(self, chat_id):
        return self.chats[chat_id]
