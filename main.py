from pytube import YouTube, Playlist

kind = int(input('For video download press 1, For playlist press 2:    '))


def completedVideo():
    print('Your video downloaded successfully')


def completedAudio():
    print('Your audio downloaded successfully')


if kind == 1:

    url = input("Enter video_URL:   ")  # Link will be downloaded  # https://www.youtube.com/watch?v=FxDlv1XKhD0
    video = YouTube(url)  # Object from YOUTUBE class

    # Video Information
    print("Video Title: ", video.title)
    print("Video Length: ", video.length, "Seconds")

    quality = int(input('for height quality press 1  for low quality press 2  for audio only press 3   '))
    filename = input('Enter filename:   ')


    def completedVideo():
        print('Your video downloaded successfully')


    def completedAudio():
        print('Your audio downloaded successfully')


    if quality == 1:
        print('Please Wait...')
        video.streams.get_highest_resolution().download(output_path='c://Users/C.M/Downloads', filename=filename)
        video.register_on_complete_callback(completedVideo())
    elif quality == 2:
        print('Please Wait...')
        video.streams.get_lowest_resolution().download(output_path='c://Users/C.M/Downloads', filename=filename)
        video.register_on_complete_callback(completedVideo())
    elif quality == 3:
        print('Please Wait...')
        video.streams.get_audio_only().download(output_path='c://Users/C.M/Downloads', filename=filename)
        video.register_on_complete_callback(completedAudio())

elif kind == 2:
    # playlist
    url = input("Enter Playlist_URL:   ")  # Link will be downloaded  # https://www.youtube.com/watch?v=NkOXBrHbqSs&list=PLMm8EjqH1EFV-jECqtMxeVMDoVkV_kJDY
    playlist = Playlist(url)  # create object

    quality = int(input('for height quality press 1  for low quality press 2  for audio only press 3   '))

    folderName = input('Enter Folder name:   ')

    count = 0

    for i in playlist.videos:
        if quality == 1:
            print('Please Wait...')
            i.streams.get_highest_resolution().download(output_path='c://Users/C.M/Downloads/' + folderName)
            i.register_on_complete_callback(completedVideo())
            count = + 1
        elif quality == 2:
            print('Please Wait...')
            i.streams.get_lowest_resolution().download(output_path='c://Users/C.M/Downloads/' + folderName)
            i.register_on_complete_callback(completedVideo())
            count = + 1
        elif quality == 3:
            print('Please Wait...')
            i.streams.get_audio_only().download(output_path='c://Users/C.M/Downloads/' + folderName)
            i.register_on_complete_callback(completedAudio())
            count = + 1

    print('Total videos: ', count, 'video')