from chatmate_platforms.telegram.message import Message
from chatmate_utils.logger import logger


class TelegramPlatform:
    def __init__(self, messenger):
        self.messenger = messenger

    def send_message(self, chant_id, text):
        logger.app_info(f"Telegram send_message {chant_id}->{text}")
        self.messenger.send_message(chant_id, text)

    def get_chats(self):
        logger.app_info(f"Telegram get_chats")
        msgs = self._get_daivinchik_msgs()
        match_msgs = [msg for msg in msgs if self.__is_match_msg(msg)]
        chat_ids = [Message().get_chat_id(msg) for msg in match_msgs]
        chats = [self.messenger.get_chat(id) for id in chat_ids]

        return chats

    def get_link_status(self, link):
        return 'active'

    def get_chat_links(self):
        logger.app_info(f"Telegram get_chat_links")
        msgs = self._get_daivinchik_msgs()
        match_msgs = [msg for msg in msgs if self.__is_match_msg(msg)]
        chat_ids = [Message().get_chat_id(msg) for msg in match_msgs]
        return chat_ids

    def get_chat_msgs(self, id):
        logger.app_info(f"Telegram get_chat_msgs {id}")
        return self.messenger.get_chat_slice(id, 300)['msgs']

    def can_like(self):
        msgs = self._get_daivinchik_msgs()
        if not msgs:
            return False

        last = msgs[-1]

        return 'photo' in last

    def like_next(self):
        self.messenger.send_message('@leomatchbot', '❤️')

    def __is_match_msg(self, msg):
        return Message().get_type(msg) == 'match'

    def _get_daivinchik_msgs(self):
        chat = self.messenger.get_chat(chat_id='@leomatchbot')
        return chat['msgs']

    def __get_chat_id(self, msg):
        words = msg.split(' ')
        chat_id = words[-1]
        return chat_id

    def get_name(self):
        return 'telegram'