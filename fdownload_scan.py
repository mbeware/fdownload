import fdownload_ytdlp
import fdownload_config
import time
from dataclasses import dataclass, field
import fdownload_queue

@dataclass
class Channel:
    url: str
    channel_name: str = ""
    provider: str = ""
    processed_video_ids: list[str] = field(default_factory=list)
    all_video_ids: list[str] = field(default_factory=list)
    new_video_ids: list[str] = field(default_factory=list)

    
#channels: list[Channel] = []
videoqueue = fdownload_queue.get_queue()

def scan_channels():
    global channels

    while True:
        loop_start_time = time.time()
        channels = [] # read from BD instead....
        for channel in channels:
            channel.all_video_ids = get_video_ids(channel)
            push_new_videos(channel)
        loop_end_time = time.time()
        loop_timeleft = fdownload_config.minimum_scan_time - (loop_end_time - loop_start_time)
        if loop_timeleft > 0:
                time.sleep(loop_timeleft)  # Sleep for a while before checking again



def push_new_videos(channel: Channel):
    
    for video_id in channel.all_video_ids:
        if video_id not in channel.processed_video_ids:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videoqueue.put(video_url)
            # # push video_url to fifo to be downloaded
            # with open(fdownload_config.DOWNLOAD_FIFO, 'a') as fifo:
            #     fifo.write(video_url + '\n')    
            #     channel.processed_video_ids.append(video_id)


    
def get_video_ids(channel:Channel) -> list[str]:
    url = channel.url
    if fdownload_ytdlp.call_ytdlp(url,fdownload_config.scan_config) == 0:
        video_ids = parse_video_ids_from_archive(fdownload_config.scan_config["--download-archive"][0])
        return video_ids
    else:
        return []       
    
def parse_video_ids_from_archive(archive_path: str) -> list[str]:
    video_ids = []
    try:
        with open(archive_path, 'r') as archive_file:
            for line in archive_file:
                video_id = line.strip()
                if video_id:
                    video_ids.append(video_id)
    except FileNotFoundError:
        pass
    return video_ids
        