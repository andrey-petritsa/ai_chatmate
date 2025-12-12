from urllib.parse import urlparse


class Message:
    def get_type(self, msg):
        invite_msg_template = 'Начинай общаться'
        if invite_msg_template in msg['text']:
            return 'match'
        else:
            return 'unknown'

    def get_chat_id(self, msg):
        text_links = [entity for entity in msg['entities'] if entity['type'] == 'text_link']
        if text_links:
            return self.__parser_user_id(text_links[0]['url'])

        raise Exception("No match id in api msg")

    def __parser_user_id(self, url):
        parsed = urlparse(url)
        user_id = parsed.path.lstrip("/")
        return f"@{user_id}"