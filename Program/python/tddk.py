from pytube import YouTube 
yt=YouTube("http://www.youtube.com/watch?v=KDiPZ1gXyMI")
streams =yt.streams
stream=streams.filter(resolution='1080p', file_extension='mp4').first()
print(stream)
