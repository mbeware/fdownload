from mbeware_db.base_repo import BaseRepository

class ChannelRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, table="channels", primary_key="url")
