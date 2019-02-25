
import subprocess
import time
import multiprocessing as mp
from queue import Queue



def convert_video_720(video_input,video_output):
	 # ffmpeg -i input.wmv -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 output.mp4
    cmds = ['ffmpeg', '-i', "/Users/leeseunghee/Documents/EC500/class_practice/Exercise2/videos/"+ video_input,'-r','30','-s','hd720',video_output]
    subprocess.call(cmds)

    return print("video convert for 720p is done")

def convert_video_480(video_input,video_output):
	cmds = ['ffmpeg', '-i', "/Users/leeseunghee/Documents/EC500/class_practice/Exercise2/videos/"+ video_input,'-r','30','-s','hd480',video_output]
	subprocess.call(cmds)

	return print("video convert for 480p is done")





# stream = ffmpeg.input('videotests/example.mov')

# video_input = "full_ball.mp4"
# video_output = "result.mp4"

# now = time.time();
# # encoding function

# convert_video(video_input, video_output)

# end = time.time();

# print("Encoding time is: ",end - now)