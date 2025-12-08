
from sqlalchemy import create_engine

# Create an engine connected to the SQLite database
engine = create_engine(f'sqlite:////tmp/fdownload.sqlite/data.db')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Channels(Base):
     __tablename__  = 'channels'
     url = Column(String, primary_key=True)
     channel_name = Column(String)

# Create all tables in the engine
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Insert records into the sportscar table
new_channel = Channels(url="test")
session.add(new_channel)

# Commit the transaction
session.commit()

