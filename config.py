import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("6226131", 12345))
      API_HASH = os.environ.get("02b6c71fee201da9cda27dc0a56483c6")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("kaunglayzz", "Ts_Bots")
      ADMIN_ID = int(os.environ.get("1731513098", 123476535 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
