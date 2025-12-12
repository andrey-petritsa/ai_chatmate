class ChatgptPageInfo:
    def get_chats(self):
        chats = self.page.locator("#history > *")

        count = chats.count()
        chats = []

        for i in range(count):
            chat = chats.nth(i)

            name = chat.inner_text().strip()

            if not name:
                continue

            chats.append(name)

        return chats