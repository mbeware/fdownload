from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
import fdownload_config
from sqlalchemy import create_engine

# Create an engine connected to the SQLite database
dbEngine = create_engine(f'sqlite:///{fdownload_config.DB_NAME}')


dbDef = declarative_base()

class dbChannels(dbDef):
    __tablename__ = 'channels'
    url = Column(String, primary_key=True)

class dbChannelSettings(dbDef):
    __tablename__ = 'channel_settings'
    url = Column(String, primary_key=True)
    name = Column(String, primary_key=True)
    value = Column(String, nullable=False)

 #   folder = Column(String)
 #   active = Column(Boolean)
 #   remove_ads = Column(Boolean)
 #   download_subtitles = Column(Boolean)
 #   merge_subtitles = Column(Boolean)

class dbChannelVideos(dbDef):
    __tablename__ = 'channel_videos'
    url = Column(String, primary_key=True)
    id = Column(String)
    downloaded = Column(DateTime)

dbDef.metadata.create_all(dbEngine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=dbEngine)
dbSession = Session()

