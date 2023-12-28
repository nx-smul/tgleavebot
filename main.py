# Remove telegram groups
# python3 -m pip install --upgrade telethon
from telethon import TelegramClient, sync
# get an Id from https://my.telegram.org/apps
api_id = 29354418
api_hash = '4f0d611620c2821a4fb2423ad5d5b2d7'
# List all the group names you want to keep, the script will delete other groups.
excluded_groups = ['','']

class TelegramAPIs(object):
    def init_client(self, session_name, api_id, api_hash):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.client.start()

    def close_client(self):
        if self.client.is_connected():
            self.client.disconnect()

    def clean(self):
        for dialog in self.client.get_dialogs():
            if hasattr(dialog.entity, "title") and dialog.entity.title not in excluded_groups:
                print('----- deleting ', dialog.entity.title)
                self.client.delete_dialog(dialog.entity)

ta = TelegramAPIs()
ta.init_client(session_name='session_name', api_id=api_id, api_hash=api_hash)
ta.clean()
ta.close_client()