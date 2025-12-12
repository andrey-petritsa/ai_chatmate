import asyncio
import time
from datetime import datetime
from types import SimpleNamespace

from pyrogram import utils as pyrogram_utils, raw
from pyrogram import Client

from chatmate_utils.env import Env


class TelegramApi:
    def __init__(self):
        tg_session = Env.load('TG_SESSION')
        tg_api_id = Env.load('TG_API_ID')
        api_hash = Env.load('TG_API_HASH')
        self.latest_limit = 100
        self.app = Client(name='tg_session', session_string=tg_session, api_id=tg_api_id, api_hash=api_hash)
        self.app.start()

    def fetch_newer(self, message_id, channel_id):
        msgs = []
        min_id = message_id
        peer = self.app.resolve_peer(channel_id)

        while True:
            limit = 100
            res = self.app.invoke(
                raw.functions.messages.GetHistory(
                    peer=peer,
                    offset_id=0,
                    offset_date=0,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=min_id,
                    hash=0,
                )
            )
            api_msgs = asyncio.get_event_loop().run_until_complete(
                pyrogram_utils.parse_messages(self.app, res, replies=0)
            )
            if not api_msgs:
                break

            msgs.extend(api_msgs)
            min_id = max(m.id for m in msgs)
        return msgs

    def fetch_all(self, channel_id):
        peer = self.app.resolve_peer(channel_id)
        all_msgs = []
        offset_id = 0
        limit = 100

        while True:
            res = self.app.invoke(
                raw.functions.messages.GetHistory(
                    peer=peer,
                    offset_id=offset_id,
                    offset_date=0,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0,
                )
            )

            msgs = asyncio.get_event_loop().run_until_complete(
                pyrogram_utils.parse_messages(self.app, res, replies=0)
            )

            if not msgs:
                break

            all_msgs.extend(msgs)
            offset_id = msgs[-1].id

            if len(msgs) < limit:
                break

        return all_msgs

    def fetch_latest_count(self, channel_id, count):
        peer = self.app.resolve_peer(channel_id)
        all_msgs = []
        offset_id = 0

        while len(all_msgs) < count:
            remaining = count - len(all_msgs)
            limit = min(100, remaining)

            res = self.app.invoke(
                raw.functions.messages.GetHistory(
                    peer=peer,
                    offset_id=offset_id,
                    offset_date=0,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0,
                )
            )

            msgs = asyncio.get_event_loop().run_until_complete(
                pyrogram_utils.parse_messages(self.app, res, replies=0)
            )

            if not msgs:
                break

            all_msgs.extend(msgs)

            offset_id = msgs[-1].id

            if len(msgs) < limit:
                break

        return all_msgs[:count]

    def fetch_latest(self, channel_id):
        peer = self.app.resolve_peer(channel_id)

        res = self.app.invoke(
            raw.functions.messages.GetHistory(
                peer=peer,
                offset_id=0,
                offset_date=0,
                add_offset=0,
                limit=self.latest_limit,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )

        msgs = asyncio.get_event_loop().run_until_complete(
            pyrogram_utils.parse_messages(self.app, res, replies=0)
        )

        return msgs

    def fetch_chats(self):
        dialogs = self.app.get_dialogs()

        chats = []
        for d in dialogs:
            chats.append({
                "id": d.chat.id,
                "title": d.chat.title or d.chat.first_name or d.chat.username
            })

        return chats

    def get_dialogs(self):
        return self.app.get_dialogs()

    def send_message(self, chat_id, msg):
        self.app.send_message(chat_id, msg)
        api_msg = SimpleNamespace(
            from_user=SimpleNamespace(
                first_name='bot',
                is_self=True,
                id='bot',
                username='bot'
            ),
            text=msg,
            photo=None,
            entities=[],
            caption=None,
            date=datetime.fromtimestamp(time.time())
        )

        return api_msg
