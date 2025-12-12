from collections import Counter

from chatmate_business.vouter.voyter_msgs import *


class Voter:
    def __init__(self):
        self.time_provider = None
        self.vote_time_start = 0

        self.user_msgs = []
        self.chatmate_msgs = []
        self.voter_msgs = []
        
        self.maximum_msgs = 10

    def declare_voting_start(self):
        self.vote_time_start = self.time_provider.get_now_date_as_timestamp()

        if len(self.user_msgs) == 0:
            ai_msgs = [self.__to_ai_msg(msg, i) for i, msg in enumerate(self.chatmate_msgs, start=1)]
            msgs = [
                DECLARE_VOTE_MSG,
                EMPTY_CHAT_MSG,
                OPTIONS_DIVIDER_MSG, *ai_msgs,
                OPTIONS_DIVIDER_MSG]
            return msgs

        chat_msgs = [self.__to_msg(msg) for msg in self.user_msgs][:self.maximum_msgs]
        ai_msgs = [self.__to_ai_msg(msg, i) for i, msg in enumerate(self.chatmate_msgs, start=1)]
        msgs = [DECLARE_VOTE_MSG,
            DIVIDER_MSG,
            *chat_msgs,
            DIVIDER_MSG,
            OPTIONS_DIVIDER_MSG,
            *ai_msgs,
            OPTIONS_DIVIDER_MSG,
        ]
        return msgs

    def __to_msg(self, msg):
        icon = '🤖' if msg['is_my'] else '❤️'
        msg = f"{icon} {msg['name']}: {msg['text']}"
        return msg

    def __to_ai_msg(self, msg, i):
        return f"{i}. {msg}"

    def declare_voting_end(self):
        if not self.has_winner():
            return [END_VOTE_MSG, NO_VOTE_MSG]
        winner_msg = self.get_winner()
        out_winner_msg = f'🎉 {winner_msg}'

        return [END_VOTE_MSG,out_winner_msg]

    def has_winner(self):
        vote_msgs = self.__get_current_vote_msgs(self.voter_msgs)
        return len(vote_msgs) >= 1

    def __get_current_vote_msgs(self, chat_msgs):
        current_vote_msgs = [msg for msg in chat_msgs if msg['date'] >= self.vote_time_start]
        int_msgs = [msg for msg in current_vote_msgs if msg['text'].isdigit()]
        uniques_msgs = self.__get_unique_msgs(int_msgs)
        vote_msgs = [msg for msg in uniques_msgs if int(msg['text']) <= len(self.chatmate_msgs)]
    
        return vote_msgs

    def get_winner(self):
        vote_msgs = self.__get_current_vote_msgs(self.voter_msgs)
        winner_index = self.__get_winner_msg_index(vote_msgs)
        winner_msg = self.chatmate_msgs[winner_index]

        self.last_winner_msg = winner_msg
        return winner_msg

    def __get_winner_msg_index(self, uniques_msgs):
        msgs_texts = [msg['text'] for msg in uniques_msgs]
        counts = Counter(msgs_texts)
        winner_index = max(counts, key=counts.get)
        return int(winner_index) - 1

    def __get_unique_msgs(self, msgs):
        unique_msgs = {}
        for msg in msgs:
            sender_id = msg["sender"]["id"]
            unique_msgs[sender_id] = msg
        return list(unique_msgs.values())

    def set_user_msgs(self, user_msgs):
        self.user_msgs = user_msgs

    def set_chatmate_msgs(self, chatmate_msgs):
        self.chatmate_msgs = chatmate_msgs

    def set_voter_msgs(self, voter_msgs):
        self.voter_msgs = voter_msgs





