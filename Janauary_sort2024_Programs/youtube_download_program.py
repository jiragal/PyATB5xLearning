from pytube import YouTube


url = input("https://www.youtube.com/watch?v=DVfXy4wlkds")
yt=YouTube(url)

#Filter audio streams and download the first one
audio_stream= yt.streams.filter(only_audio=True).first()
audio_stream.download()
