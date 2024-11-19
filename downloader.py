import yt_dlp as ydl

def download_video(url, download_path):
    options = {
        'format': 'best',  # выбираем лучший формат
        'outtmpl': download_path + '/%(title)s.%(ext)s',
        'progress_hooks': [lambda d: print(f"Downloading {d['filename']} - {d['_percent_str']} completed.")],
        'noplaylist': True
    }

    with ydl.YoutubeDL(options) as ydl_instance:
        info_dict = ydl_instance.extract_info(url, download=True)
        video_title = info_dict.get("title", "video")
        video_ext = info_dict.get("ext", "mp4")
        print(f"Video '{video_title}.{video_ext}' has been downloaded successfully!")

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
download_path = 'data/'
download_video(url, download_path)
