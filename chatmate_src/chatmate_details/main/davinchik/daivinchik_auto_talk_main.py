import time

from chatmate_business.chat import Chat
from chatmate_business.usecases.send_message_command import SendMessageCommand
from chatmate_details.chatmates.deepseek.deepseek_assistant import DeepseekAssistant
from chatmate_details.repository.in_file_chat_repository import InFileChatRepository
from chatmate_details.telegram.client.telegram_messenger import TelegramMessenger
from chatmate_platforms.telegram.telegramplatform import TelegramPlatform
from chatmate_business.usecases.get_chats_command import GetChatsCommand

class DaivinchikMain:
    def __init__(self):
        messenger = TelegramMessenger()
        assistant = DeepseekAssistant()
        platform = TelegramPlatform(messenger)

        self.send_message_command = SendMessageCommand(platform=platform, assistant=assistant)
        self.get_chats_command = GetChatsCommand(platform=platform)
        self.file_repository = InFileChatRepository()
        self.chat = Chat()



    def run(self):
        while True:
            chats = self.get_chats_command.execute()

            for chat in chats:
                chat = self.send_message_command.execute(chat)
                self.file_repository.save(chat)
                time.sleep(30)
            time.sleep(60*30)


if __name__ == '__main__':
    main = DaivinchikMain()
    main.run()
