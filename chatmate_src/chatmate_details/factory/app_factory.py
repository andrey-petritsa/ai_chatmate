from chatmate_business.usecases.voter_interactor import VoterInteractor
from chatmate_business.vouter.voter import Voter
from chatmate_details.chatmates.deepseek.deepseek_assistant import DeepseekAssistant
from chatmate_details.telegram.bot.telegram_bot_voter_port import TelegramBotVoterPort
from chatmate_details.telegram.client.telegram_messenger import TelegramMessenger
from chatmate_platforms.telegram.telegramplatform import TelegramPlatform
from chatmate_business.usecases.get_chats_command import GetChatsCommand
from chatmate_utils.time_provider import TimeProvider
from chatmate_details.repository.in_file_link_repository import InFileLinkRepository



class AppFactory:
    telegram_platform = TelegramPlatform(TelegramMessenger())

    @classmethod
    def create_voter_interactor(cls):
        voter = Voter()
        voter.time_provider = TimeProvider()
        interactor = VoterInteractor()
        interactor.voter = voter
        interactor.platform = cls.telegram_platform
        interactor.chatmate_assistant = DeepseekAssistant()
        interactor.voter_port = TelegramBotVoterPort()

        return interactor

    @classmethod
    def create_get_chats_command(cls):
        cmd = GetChatsCommand()
        cmd.platform = cls.telegram_platform
        cmd.link_repository = InFileLinkRepository()
        return cmd