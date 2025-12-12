from datetime import datetime, timezone


class TimeProvider:
    def get_now_date(self):
        now = datetime.now(timezone.utc)
        return now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    def get_now_date_as_timestamp(self):
        now = datetime.now(timezone.utc)
        return int(now.timestamp())