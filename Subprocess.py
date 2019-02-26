
import subprocess
from subprocess import check_output
import time
import multiprocessing as mp
from queue import Queue
import testing as test


def convert_video_720(video_input,video_output):
	# ffmpeg -i input.wmv -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 output.mp4
	cmds = ['ffmpeg', '-i', "/Users/leeseunghee/Documents/Exercise2/videos/"+ video_input,'-r','30','-s','hd720',video_output]
	subprocess.call(cmds)
	dur1 = test.test_duration("full_ball.mp4")
	filename = "result720.mp4"
	dur2 = str(check_output('ffprobe -i  "'+filename+'" 2>&1 |grep "Duration"',shell=True)) 
	dur2 = dur2.split(",")[0].split("Duration:")[1].strip()

	h1, m1, s1 = dur2.split(':')
	dur2_ = int(h1) * 3600 + int(m1) * 60 + float(s1)

	print(dur1,dur2_)

	test.asserting(dur1,dur2_)
	return print("video convert for 720p is done")

def convert_video_480(video_input,video_output):
	cmds = ['ffmpeg', '-i', "/Users/leeseunghee/Documents/Exercise2/videos/"+ video_input,'-r','30','-s','hd480',video_output]
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