from pytube import YouTube


def download_video(url):
    yt=YouTube(url) stream
    =yt.streams.filter( adaptive=True,file_extension='mp4').order_by('resolution=1080p').desc().first()stream.download()
    
    url=input("https://youtube.com/shorts/4uqvZtHzbhs?si=5lMyrD_B39PlAemU")
    download_video(url)