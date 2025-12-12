from chatmate_utils.logger import logger


class VoterInteractor:
    def __init__(self):
        self.platform = None
        self.voter_port = None
        self.chat_port = None
        self.chatmate_assistant = None
        self.voter = None

    def start_vote(self):
        logger.app_info(f"Start vote for chat: {self.chat['id']}")
        self.voter.set_user_msgs(self.chat['msgs'])
        chatmate_msgs = self.chatmate_assistant.generate_messages(self.chat)
        self.voter.set_chatmate_msgs(chatmate_msgs)

        msgs_str = "\n".join(self.voter.declare_voting_start())
        logger.app_info(f"Send message to voter_port")
        self.voter_port.send_message(msgs_str)

    def end_vote(self):
        logger.app_info(f"End vote for chat: {self.chat['id']}")
        self.voter.set_voter_msgs(self.voter_port.get_messages())
        msgs_str = "\n".join(self.voter.declare_voting_end())
        self.voter_port.send_message(msgs_str)
        if self.voter.has_winner():
            self.platform.send_message(self.chat['id'], self.voter.last_winner_msg)

    def set_chat(self, chat):
        self.chat = chat