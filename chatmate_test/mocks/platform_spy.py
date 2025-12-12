class PlatformSpy:
    def __init__(self):
        self.events = []
        self.chats = [
            {
                'id':1,
                'msgs':[
                    {'date':1, 'text':'Тест1', 'name':'bot', 'is_my':True},
                    {'date':2, 'text':'Тест2', 'name':'human', 'is_my':False}
                ],
            }
        ]

    def send_message(self, person_id, message):
        event = f"SendMessage {person_id}->{message}"
        self.events.append(event)

    def get_chat_links(self):
        links = [1]
        return links

    def get_chat_msgs(self, id):
        return self.chats[0]['msgs']

    def get_link_status(self, link):
        return 'active'

    def get_chats(self):
        event = f"get_chats"
        self.events.append(event)
        return self.chats

    def get_name(self):
        return "spy"

