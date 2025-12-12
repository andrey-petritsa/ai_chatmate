import logging

logging.root.handlers.clear()
logging.root.setLevel(logging.CRITICAL + 1)

APP_INFO = 25
logging.addLevelName(APP_INFO, "APP_INFO")

def app_info(self, message, *args, **kwargs):
    if self.isEnabledFor(APP_INFO):
        self._log(APP_INFO, message, args, **kwargs)
logging.Logger.app_info = app_info

logger = logging.getLogger("chatmate")
logger.setLevel(APP_INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s APP_INFO %(message)s", "%d.%m.%Y %H:%M"))
logger.addHandler(handler)
logger.propagate = False