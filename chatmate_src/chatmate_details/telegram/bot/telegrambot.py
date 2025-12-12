from chatmate_utils.time_provider import TimeProvider


class TelegramBot:
    def __init__(self, telegram_api):
        self.last_update_id = None
        self.telegram_api = telegram_api

        self.time_provider = TimeProvider()

    def send_message(self, text, group_id):
        self.telegram_api.send_message(text, group_id)

    def get_messages_since(self, timestamp):
        if not self.last_update_id:
            updates = self.telegram_api.get_updates()
        else:
            updates = self.telegram_api.get_updates(self.last_update_id + 1)

        updates = updates['result']

        message_updates = self.filter_message_updates(updates)
        since_updates = self.__get_since(message_updates, timestamp)

        msgs = []
        for update in since_updates:
            msgs.append(self.__to_msg(update))

        if len(since_updates) != 0:
            self.last_update_id = message_updates[-1]['update_id']
        return msgs
    
    def filter_message_updates(self, updates):
        return [update for update in updates if 'message' in update and 'text' in update['message']]

    def __get_since(self, updates, timestamp):
        new_updates = []
        for update in updates:
            if update['message']['date'] >= timestamp:
                new_updates.append(update)
        return new_updates

    def __to_msg(self, update):
        tel_msg = update['message']
        user = tel_msg['from']
        first_name = user.get('first_name', '---')
        last_name = user.get('last_name', '---')
        msg = {'id':user['id'], 'first_name':first_name, 'last_name':last_name, 'date':tel_msg['date'], 'text':tel_msg['text']}

        return msg