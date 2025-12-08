import fdownload_config 

from sqlalchemy import delete



from fdownload_channels_db import dbDef, dbEngine,dbSession, dbChannels, dbChannelSettings, dbChannelVideos


def add_channel(purl:str, pname:str|None=None, pfolder:str|None=None):
    global dbSession
    new_channel = dbChannels(url=purl)
    dbSession.add(new_channel)

    cname = pname if pname else purl.split("/")[-1]
    new_settings = dbChannelSettings(url=purl, name="name", value=cname)
    dbSession.add(new_settings)

    cfolder = pfolder if pfolder else f"{fdownload_config.DEFAULT_DOWNLOAD_PATH}{cname}"
    new_settings = dbChannelSettings(url=purl, name="folder", value=cfolder)
    dbSession.add(new_settings)

    # Add default settings
    for sname,sval in fdownload_config.default_settings.items():
        new_setting = dbChannelSettings(url=purl, name=sname, value=sval)
        dbSession.add(new_setting)  
    # Commit the transaction
    dbSession.commit()

def remove_channel(purl:str):
    global dbSession
    # Remove from dbChannels
    channel = dbSession.query(dbChannels).filter(dbChannels.url == purl).first()
    if channel:
        # Remove from dbChannelSettings
        dbSession.execute(delete(dbChannelSettings).where(dbChannelSettings.url == purl))
        # Remove from dbChannelVideos
        dbSession.execute(delete(dbChannelVideos).where(dbChannelVideos.url == purl))
        dbSession.delete(channel)
    # Commit the transaction
        dbSession.commit()
    else:
        print(f"Channel with URL {purl} not found.")

def get_all_channels():
    global dbSession
    channels = dbSession.query(dbChannels).all()
    result = []
    for ch in channels:
        settings = dbSession.query(dbChannelSettings).filter(dbChannelSettings.url == ch.url).all()
        setting_dict = {s.name :s.value for s in settings}
        result.append({
            "url": ch.url,
            "name": setting_dict["name"] # type: ignore
        })
    return result


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
