def download(yt):
    ys = yt.streams.get_highest_resolution()
    ys.download('../Downloads')