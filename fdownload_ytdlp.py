import subprocess
import sys
def call_ytdlp(url:str, config:dict) -> int:    
    param_list = []
    for key, values in config:
        if values[1]:  # If active
            if isinstance(values[0], bool) and values[0]:
                param_list.append(key)
            else:
                param_list.append(key)
                param_list.append(str(values[0]))
    cmd = ['yt-dlp'] + param_list + [url]
    try:
        result = subprocess.run(cmd, check=True, capture_output=False) # Keep capture_output=False if you want to see yt-dlp's progress
        if result.returncode == 0:
            pass
        return result.returncode
    
    except subprocess.CalledProcessError as e:
        sys.exit(1)
        return e.returncode
    except FileNotFoundError:
        sys.exit(1)     
        return -1
               
    