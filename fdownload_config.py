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


minimum_scan_time = 600  # in seconds
DOWNLOAD_FIFO = '/tmp/fdownload_fifo'
DB_LOCATION = "/tmp/fdownload.sqlite"
