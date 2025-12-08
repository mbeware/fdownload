#AllParam = {"pname":[value,active]}
## issue : can repete a key....


scan_config ={ "--concurrent-fragments":[4,True],
               "--force-write-archive":[True,True],
               "--skip-download":[True,True],
               "-P":['/mnt/AllVideo/0082-youtube',True],
#               "-P":['temp:tmp',True],
               "--download-archive":['',True],
               "--yes-playlist":[True,True],
               "-O":['%(id)s',False],
               "--flat-playlist":[True,True],
               "--progress":[True,True],
               "-q":[True,True],
}  
download_config ={ "--concurrent-fragments":[4,True],
               "--force-write-archive":[True,True],
               "--no-skip-download":[True,True],            
                "-P":['/mnt/AllVideo/0082-youtube',True],
#                "-P":['temp:tmp',True],
                "--download-archive":['',True],
                "--yes-playlist":[True,True],
                "-O":['%(id)s',False],
                "--progress":[True,True],
                "-q":[True,True],
}



default_settings = {
    "active": "True", 
    "remove_ads": "False",
    "download_subtitles": "False",
    "merge_subtitles": "False",
    "video_description": "False",
    "download_shorts": "True", # [url]/shorts
    "download_videos": "True", # [url]/videos
    "download_completed_live": "True", # was_live=True, ended_live=True, is_live=False
}

DEFAULT_DOWNLOAD_PATH = "/mnt/AllVideo/0082-youtube/"
minimum_scan_time = 600  # in seconds
DOWNLOAD_FIFO = '/tmp/fdownload_fifo'
DB_LOCATION = "/tmp/fdownload.sqlite"
DB_NAME = f"{DB_LOCATION}/data.db"