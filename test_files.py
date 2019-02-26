
from subprocess import check_output
from pytest import approx
import os
import queue
import time


def test_duration(filename):

	origin_file_name = "full_ball.mp4"
	# result_file_name = "result720.mp4"
	print("hello")
	# filename = "/Users/leeseunghee/Documents/Exercise2/" +filename
	#For Linux
	a_origin = str(check_output('ffprobe -i  "'+origin_file_name+'" 2>&1 |grep "Duration"',shell=True)) 

	a_origin = a_origin.split(",")[0].split("Duration:")[1].strip()

	h1, m1, s1 = a_origin.split(':')
	duration_origin = int(h1) * 3600 + int(m1) * 60 + float(s1)

	

	return duration_origin

def asserting(dur1,dur2):

	assert dur1== approx(dur2)
	return print("origin duration:",dur1, " result duration:", dur2)
