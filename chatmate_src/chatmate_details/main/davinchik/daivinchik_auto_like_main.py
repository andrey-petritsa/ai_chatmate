import time

from chatmate_details.telegram.client.telegram_messenger import TelegramMessenger
from chatmate_platforms.telegram.telegramplatform import TelegramPlatform



class DaivinchikMain:
    def __init__(self):
        self.messenger = TelegramMessenger()
        self.platform = TelegramPlatform(self.messenger)

    def run(self):
        self.messenger.send_message('@leomatchbot', 'Продолжить смотреть анкеты')
        while True:
            if self.platform.can_like():
                self.platform.like_next()
            time.sleep(60)

if __name__ == '__main__':
    main = DaivinchikMain()
    main.run()
