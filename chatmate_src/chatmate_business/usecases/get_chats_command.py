from chatmate_business.chat import Chat


class GetChatsCommand:
    def __init__(self):
        self.platform = None
        self.link_repository = None

    def execute(self):
        platform_name = self.platform.get_name()
        links = self.link_repository.get_links(platform_name)
        chats = [self.__to_chat(link) for link in links]
        valid_chats = [chat for chat in chats if Chat().should_write(chat)]

        return valid_chats

    def __to_chat(self, link):
        return {'id': link['id'], 'msgs': self.platform.get_chat_msgs(link['id'])}
