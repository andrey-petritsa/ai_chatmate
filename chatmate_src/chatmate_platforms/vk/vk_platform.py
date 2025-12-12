from chatmate_business.chat import Chat


class VkDatePlatform:
    service_chat = {
        "id":1,
        "name":"service",
        "messages":[]
    }

    def __init__(self, vk_date_api):
        self.__vk_date_api = vk_date_api
        self.chat = Chat()

    def send_message(self, message):
        self.__vk_date_api.send_message(message)

    def get_chats(self):
        get_chats_response = self.__vk_date_api.get_chats()
        get_chats_response = get_chats_response.json()
        chats = []
        for vk_chat in get_chats_response["chats"]:
            if not self.__is_service_chat(vk_chat) and not self.__is_invalid_chat(vk_chat):
                chats.append(self.__convert_to_chat(vk_chat))

        return chats

    def get_chat(self, user_id):
        get_history_response = self.__vk_date_api.get_history(user_id)
        history = get_history_response.json()
        messages = []
        for vk_message in history['messages']:
            messages.append(self.__convert_to_message(vk_message))

        chat = {'id':user_id, 'messages':messages, 'name':str(user_id)}
        return chat

    def __convert_to_chat(self, vk_api_chat):
        user_id = vk_api_chat['user_id']

        if self.__is_service_chat(vk_api_chat):
            return self.service_chat

        user_name = vk_api_chat["user"]["name"]
        return {
            "id":user_id,
            "name":user_name,
            "messages":self.__get_messages(user_id)
        }

    def __get_messages(self, user_id):
        messages = []
        get_history_response = self.__vk_date_api.get_history(user_id)
        get_history_response = get_history_response.json()
        for vk_message in get_history_response['messages']:
            messages.append(self.__convert_to_message(vk_message))

        return messages

    

    def __convert_to_message(self, vk_api_message):
        return {
            'text':vk_api_message['content'],
            'date':vk_api_message['created_at'],
            'name':self.__get_user_name(vk_api_message)
        }

    def __get_user_name(self, message):
        if message['is_my']:
            return 'bot'
        else:
            return 'girl'

    def __is_service_chat(self, chat):
        return chat['user_id'] == 1

    def __is_invalid_chat(self, chat):
        return chat['type'] == 'invalid'

    def get_chats_info(self):
        get_chats_response = self.__vk_date_api.get_chats()
        get_chats_response = get_chats_response.json()
        chats = []
        for vk_chat in get_chats_response["chats"]:
            if not self.__is_service_chat(vk_chat) and not self.__is_invalid_chat(vk_chat):
                chats.append(self.__convert_to_chat_info(vk_chat))

        return chats

    def __convert_to_chat_info(self, vk_chat):
        last_vk_message = vk_chat['message']
        last_message = self.__convert_to_message(last_vk_message)

        chat_info = {
            'id':vk_chat['user_id'],
            'name':vk_chat['user']['name'],
            'avatar_url':vk_chat['user']['preview_url'],
            'last_message_timedelta': self.chat.get_last_message_timedelta(last_message),
            'is_answered': self.chat.is_answered(last_message),
        }


        return chat_info
