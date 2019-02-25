import os
from Subprocess import convert_video_720
from Subprocess import convert_video_480
import threading
import queue
import time



def main():


	q1 = queue.Queue()
	q2 = queue.Queue()

	inputPath = "/Users/leeseunghee/Documents/EC500/class_practice/Exercise2/videos"
	files = os.listdir(inputPath)

	for file in files:
		q1.put(file)
	while not q1.empty():
		video_input = q1.get()

	for file in files:
		q2.put(file)
	while not q1.empty():
		video_input = q2.get()

	print("hi")

	video_output1 = "result720.mp4"
	video_output2 = "result420.mp4"

	t1 = threading.Thread(target = convert_video_720, args = (video_input,video_output1))
	t2 = threading.Thread(target = convert_video_480, args = (video_input,video_output2))

	now = time.time();
	
	t1.start()
	t2.start()

	end = time.time();

	print("Encoding time is: ",end - now)



if __name__ == '__main__':
	main()