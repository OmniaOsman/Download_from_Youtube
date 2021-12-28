from pytube import YouTube

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
    print('PleaseWait...')
    video.streams.get_lowest_resolution().download(output_path='c://Users/C.M/Downloads', filename=filename)
    video.register_on_complete_callback(completedVideo())
elif quality == 3:
    print('PleaseWait...')
    video.streams.get_audio_only().download(output_path='c://Users/C.M/Downloads', filename=filename)
    video.register_on_complete_callback(completedAudio())
