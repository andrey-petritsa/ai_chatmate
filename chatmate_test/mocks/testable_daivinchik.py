from chatmate_platforms.telegram.telegramplatform import TelegramPlatform


class TestableTelegramPlatform(TelegramPlatform):
    def __init__(self, messenger):
        super().__init__(messenger)
        self.msgs = []

    def _get_daivinchik_msgs(self):
        return self.msgs