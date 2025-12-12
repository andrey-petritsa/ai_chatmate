import requests

class TelegramBotApi:
    def __init__(self, token):
        self.last_response = None
        self.tg_bot_token = token

    def get_updates(self, last_update_id=None):
        url = f"https://api.telegram.org/bot{self.tg_bot_token}/getUpdates"
        if last_update_id:
            url += f"?offset={last_update_id}"
        response = requests.get(url)
        self.last_response = response
        return response.json()

    def send_message(self, chat_id, text):
        url = f"https://api.telegram.org/bot{self.tg_bot_token}/sendMessage"
        params = {
            "chat_id":chat_id,
            "text":text
        }
        response = requests.post(url, params=params)
        self.last_response = response
        return response.json()

    def get_messages(self, chat_id):
        updates = self.get_updates()
        messages = []

        if 'result' in updates:
            for update in updates['result']:
                if 'message' in update and update['message']['chat']['id'] == int(chat_id) and 'text' in update['message']:
                    messages.append(update['message'])

        return messages
