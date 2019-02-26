import os
from Subprocess import convert_video_720
from Subprocess import convert_video_480
import test_files as test
import threading
import queue
import time



def main():


	q1 = queue.Queue()
	q2 = queue.Queue()

	inputPath = "/Users/leeseunghee/Documents/Exercise2/videos"
	video_input1 =""
	video_input2 =""

	files = os.listdir(inputPath)

	for file in files:
		q1.put(file)
	while not q1.empty():
		video_input1 = q1.get()

	print("before",files)

	for file in files:
		q2.put(file)
	while not q2.empty():
		video_input2 = q2.get()


	video_output1 = "result720.mp4"
	video_output2 = "result420.mp4"


	t1 = threading.Thread(target = convert_video_720, args = (video_input1,video_output1))
	t2 = threading.Thread(target = convert_video_480, args = (video_input2,video_output2))

	t1.start()
	t2.start()


	# dur1 = test.test_duration("full_ball.mp4")
	# dur2 = test.test_duration("result720.mp4")

	# test.asserting(t1[0],t2[0])


if __name__ == '__main__':
	main()