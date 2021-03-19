
def print_video_info(yt):
    print()
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length, "senconds")
    print("Ratings: ", yt.rating)
    print()
    print(yt.streams.filter(only_audio=True))
    print()
    print(yt.streams.filter(only_video=True))
    print()
    print(yt.streams.filter(progressive=True))
