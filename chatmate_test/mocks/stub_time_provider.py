class StubTimeProvider:
    def __init__(self):
        self.now_date = '2025-01-02T18:05:25.000Z'
        self.now_date_timestamp = 1

    def get_now_date(self):
        return self.now_date

    def get_now_date_as_timestamp(self):
        return self.now_date_timestamp
