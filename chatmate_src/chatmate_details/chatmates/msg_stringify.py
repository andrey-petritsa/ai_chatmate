class MsgStringify:
    def to_str_msg(msg):
        mark = "(+)" if msg['is_my'] else "(-)"
        return f"{mark} {msg['name']}: {msg['text']}!"