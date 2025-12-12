import json
import os


class InFileChatRepository:
    path_to_chats = "output/chats"

    def save(self, chat):
        chat_path = self.__get_chat_path(chat['id'])
        f = open(chat_path, 'w')
        json_chat = json.dumps(chat, ensure_ascii=False, indent=4)
        f.write(json_chat)
        f.close()

    def find_chat(self, user_id):
        chat_path = self.__get_chat_path(user_id)
        f = open(chat_path, 'r')
        chat = json.loads(f.read())
        f.close()
        return chat

    def __get_chat_path(self, user_id):
        return f"{self.path_to_chats}/{user_id}.json"

    def find_all_chats(self):
        files = []

        for file_name in os.listdir(self.path_to_chats):
            file_path = os.path.join(self.path_to_chats, file_name)
            files.append(open(file_path, 'r'))

        chats = []

        for f in files:
            chat = json.loads(f.read())
            chats.append(chat)

        return chats
