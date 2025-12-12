from dotenv import dotenv_values

class Env:
    @classmethod
    def load(cls, name):
        ENV_VARS = dotenv_values("settings/.env")
        return ENV_VARS[name]
