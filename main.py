from pytube import YouTube, Playlist

kind = int(input('For video download press 1, For playlist press 2:    '))


def completedVideo():
    print('Your video downloaded successfully')


def completedAudio():
    print('Your audio downloaded successfully')


def highQuality():
    print('Please Wait...')
    video.streams.get_highest_resolution().download(output_path='c://Users/C.M/Downloads', filename=filename)
    video.register_on_complete_callback(completedVideo())


def lowQuality():
    print('Please Wait...')
    video.streams.get_lowest_resolution().download(output_path='c://Users/C.M/Downloads', filename=filename)
    video.register_on_complete_callback(completedVideo())

def audio():
    print('Please Wait...')
    video.streams.get_audio_only().download(output_path='c://Users/C.M/Downloads', filename=filename)
    video.register_on_complete_callback(completedAudio())


if kind == 1:

    url = input("Enter video_URL:   ")  # Link will be downloaded  # https://www.youtube.com/watch?v=FxDlv1XKhD0
    video = YouTube(url)  # Object from YOUTUBE class

    # Video Information
    print("Video Title: ", video.title)
    print("Video Length: ", video.length, "Seconds")

    quality = int(input('for height quality press 1  for low quality press 2  for audio only press 3   '))
    filename = input('Enter filename:   ')

    if quality == 1:
        highQuality()
    elif quality == 2:
        lowQuality()
    elif quality == 3:
        audio()

elif kind == 2:
    # playlist
    url = input("Enter Playlist_URL:   ")  # Link will be downloaded  # https://www.youtube.com/watch?v=1ybX_oVEbzc&list=PLMm8EjqH1EFWWKAeZFMmnbvnDML6NhY35
    playlist = Playlist(url)  # create object

    quality = int(input('for height quality press 1  for low quality press 2  for audio only press 3   '))

    folderName = input('Enter Folder name:   ')

    count = 0

    for i in playlist.videos:
        if quality == 1:
            highQuality()
        elif quality == 2:
            lowQuality()
        elif quality == 3:
            audio()

        count = count + 1

    print('Total downloads is: ', count)
