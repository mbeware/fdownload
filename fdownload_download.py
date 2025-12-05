import fdownload_config
import fdownload_ytdlp
import fdownload_queue

videoqueue = fdownload_queue.get_queue()

def download_videos():
    # Implémentation du téléchargement des vidéos
    # download all video from fifo
    while True:
        video_url=videoqueue.get()
        if fdownload_ytdlp.call_ytdlp(video_url,fdownload_config.download_config) ==0:
            pass
        
