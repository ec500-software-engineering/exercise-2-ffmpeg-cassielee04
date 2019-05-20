import os
#from Subprocess import *
# from Subprocess import convert_video_480
import threading
import time
import subprocess
import os
import json
import multiprocessing as mp
import queue
from pytest import approx



"""
input files to the queue
return finalized Q
"""
def fetch_files(inputpath):  

	Vid_Q = queue.Queue() 

	vid_requests_path = inputpath
	files = os.listdir(vid_requests_path)

	for video in files:
		# detect file type (MP4)
		extension = video.split('.')
		if ( extension[-1] == 'mp4' or  
			extension[-1] == '.avi' or 
			extension[-1] == '.flv' or 
			extension[-1] == '.wmv' or 
			extension[-1] == '.mov'):
				Vid_Q.put(video)

		else:
			pass

	return Vid_Q



def convert_video_720(inputpath):
	 # ffmpeg -i input.wmv -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 output.mp4

		if not os.path.exists('./output_videos/'):  # create output folder
			os.mkdir('./output_videos/')
		else:
		    outputpath = "./output_videos/"+inputpath[:-4]+"_720p.mp4"
		    cmds = ['ffmpeg', '-i', './videos/'+ inputpath , '-r','30','-s','hd720',outputpath]
		    conversion1 = subprocess.Popen(cmds)
		    #init_counter = init_counter+1
		    #counter_720 = counter_720+1

		    wait1 = conversion1.wait()
		    #done_counter = done_counter+1

		#if(init_counter != done_counter):
		#	print("error occurred the initial file is" + init_counter+ "the finished task is " + done_counter)
		
		#else:
		#	print("Finished" + counter_720 +  "Video720\n")
	

def convert_video_480(inputpath):

		if not os.path.exists('./output_videos/'):  # create output folder
			os.mkdir('./output_videos/')

		else:    
			outputpath = "./output_videos/"+inputpath[:-4]+"_480p.mp4"
			cmds = ['ffmpeg', '-i','./videos/'+ inputpath, '-r','30','-s','hd480',outputpath]
			conversion2 = subprocess.Popen(cmds)
			#init_counter = init_counter+1
			#counter_480 = counter_480+1

			wait2 = conversion2.wait()
			#done_counter = done_counter+1

		#if(init_counter != done_counter):
		#	print("error occurred the initial file is" + init_counter+ "the finished task is " + done_counter)
		
		#else:
		#	print("Finished" + counter_480 +  "Video480\n")



def Threading(Vid_Q):
	if(Vid_Q.empty()): #no videos
		print("No Files to Convert")
		pass
	else:

		#while the queue has video files run convert until nofiles left
		while (not Vid_Q.empty()):

			video = Vid_Q.get()

			#one thread per one resolution 

			convert_480 = threading.Thread(target=convert_video_480, args=(video,)) # convert to 480
			convert_480.start()
			convert_720 = threading.Thread(target=convert_video_720, args=(video,)) # convert to 720
			convert_720.start()

			counvert_480.join()
			convert_720.join()


	#print(str(counter) + "files are converting in total")




# def ffprobe(inputfile,outputfile):
# 	input_info = subprocess.check_output(['ffprobe', '-v', 'warning',
#                                     '-print_format', 'json',
#                                     '-show_streams',
#                                     '-show_format',
#                                     inputfile],text=True)
# 	input_data = json.loads(input_info)

# 	output_info = subprocess.check_output(['ffprobe', '-v', 'warning',
#                                     '-print_format', 'json',
#                                     '-show_streams',
#                                     '-show_format',
#                                     outputfile],text=True)
# 	output_data = json.loads(output_info)

# 	ori_duration = float(input_data['streams'][0]['duration'])
# 	out_duration = float(output_data['streams'][0]['duration'])

# 	assert ori_duration == approx(out_duration)


def main():

	inputPath = "./videos"
	input_q = fetch_files(inputPath)




	init_counter = 0
	done_counter = 0
	counter_480=0
	counter_720 =0
	outputPath_480 =''
	outputPath_720 = ''

	#START Threading
	conversion = threading.Thread(target=Threading, args =(input_q,))

	conversion.start()




if __name__ == '__main__':
	main()

