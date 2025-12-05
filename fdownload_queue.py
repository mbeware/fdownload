from persistqueue import FIFOSQLiteQueue
import fdownload_config

videoqueue = FIFOSQLiteQueue(path=fdownload_config.DB_LOCATION, multithreading=True)    

def get_queue():
    return videoqueue
