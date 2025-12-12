from chatmate_utils.time_provider import TimeProvider


class Chat:
    def __init__(self):
        self.time_provider = TimeProvider()

    def should_write(cls, chat):
        if not chat['msgs']:
            return True

        if cls.__is_last_message_too_old(chat):
            return True

        return not cls.is_answered(chat)

    def is_answered(self, chat):
        last = chat['msgs'][-1]
        return last['is_my'] == True

    def __is_last_message_too_old(self, chat):
        now_date_timestamp = self.time_provider.get_now_date_as_timestamp()
        last_msg_date_timestamp = chat['msgs'][-1]['date']
        return self.is_diff_more_or_equal_3_hours(now_date_timestamp, last_msg_date_timestamp)

    def is_diff_more_or_equal_3_hours(self, now_ts, last_ts):
        THREE_HOURS = 3 * 60 * 60
        return (now_ts - last_ts) >= THREE_HOURS