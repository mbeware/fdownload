from mbeware_db.easydb import Database
from fdownload_channels_db import ChannelRepository
import fdownload_config 

def setup_schema(db):
    conn = db.get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS channels (
            url TEST NOT NULL,
            channel_name TEXT NULL
        )
    """)
    conn.commit()


db = Database(fdownload_config.DB_LOCATION)
setup_schema(db)
channel = ChannelRepository(db)

    # CREATE
#    channel.create({"username": "martin", "email": "martin@example.com"})






if __name__ == "__main__":
    pass
#    db = Database(fdownload_config.DB_LOCATION)
#    setup_schema(db)

#    channel = ChannelRepository(db)

    # CREATE
#    channel.create({"username": "martin", "email": "martin@example.com"})

    # READ
#    print(channel.read(1))

    # UPDATE
#    channel.update(1, {"email": "martin.new@example.com"})

    # LIST
#    print(channel.list_all())

    # DELETE
#    channel.delete(1)

#    db.close()
