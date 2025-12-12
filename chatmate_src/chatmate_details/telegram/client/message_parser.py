class MessageParser:
    def to_msg(self, api_msg):
        name = self.__get_user_name(api_msg)
        text = self.get_text(api_msg)
        is_my = api_msg.from_user.is_self
        sender = self.get_sender(api_msg)
        entities = self.__get_entities(api_msg)
        date = int(api_msg.date.timestamp())

        msg = {'name':name, 'text':text, 'is_my':is_my, 'entities':entities, 'sender':sender, 'date':date}
        if api_msg.photo:
            msg['photo'] = self.__get_photo(api_msg)

        return msg

    def __get_user_name(self, api_msg):
        return api_msg.from_user.first_name or 'Без имени'

    def __get_entities(self, api_msg):
        entities = api_msg.entities or []
        api_text_links = [entity for entity in entities if entity.type.name == 'TEXT_LINK']
        text_links = [self.__to_text_link(api_text_link) for api_text_link in api_text_links]
        return text_links

    def __get_photo(self, api_msg):
        caption = api_msg.caption or ""
        file_id = api_msg.photo.file_id
        return {'caption':caption, 'file_id':file_id}

    def __get_caption(self, api_msg):
        return api_msg.caption or ""

    def __to_text_link(self, api_text_link):
        return {'name':api_text_link.type.name, 'url':api_text_link.url, 'type':'text_link'}

    def get_sender(self, api_msg):
        return {'id':api_msg.from_user.id, 'nick':api_msg.from_user.username}

    def get_text(self, api_msg):
        return api_msg.text or ""
