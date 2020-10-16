from moviepy.editor import VideoFileClip
from termcolor import colored
from colorama import init, Fore, Back


# Getting The Base Information 
mp4_file = input("Enter The Path Of The Mp4 File                  : ")
name_of_mp3_file = input("Enter The Name You Want To Give To The Mp3 File : ")

# A If Loop that adds .mp3 at the last if it is not added by the user 
if 'mp3' in name_of_mp3_file:
    pass
else:
    name_of_mp3_file = (name_of_mp3_file + '.mp3')

# The Main Process Starts Here :-
video = VideoFileClip(mp4_file)
audioclip = video.audio
audioclip.write_audiofile(name_of_mp3_file)
audioclip.close()
video.close()

main.mainloop()

