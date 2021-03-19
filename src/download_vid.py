def download(yt):
    check_input = False
    while (check_input == False):
        audio = input("Do you want just the audio? (y/n): ")
        if audio == 'y':
            ys = yt.streams.get_audio_only()
            check_input = True
        elif audio == 'n':
            ys = yt.streams.get_highest_resolution()
            check_input = True
        else:
            print("You need to choose either [y] or [n]")
            
    ys.download('../Downloads')