import display_info
import download_vid
from pytube import YouTube

def main():
    link = input("Enter link to download: ")
    yt = YouTube(link)

    display_info.print_video_info(yt)
    download_vid.download(yt)

    print()
    print("Video downloaded in <Downloads> directory!")

if __name__ == "__main__":
    main()
