
import threading
import subprocess
import os
import queue
# from pytest import approx



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

		# if not os.path.exists('./output_videos/'):  # create output folder
		# 	os.mkdir('./output_videos/')
	    outputpath = "./output_videos/"+inputpath[:-4]+"_720p.mp4"
	    cmds = ['ffmpeg', '-i', './videos/'+ inputpath , '-r','30','-s','hd720',outputpath]
	    conversion1 = subprocess.Popen(cmds)
	    #init_counter = init_counter+1
	    #counter_720 = counter_720+1

	    conversion1.wait()

	    print("conversion for " + inputpath +" _720 is complete" )
		    #done_counter = done_counter+1

		#if(init_counter != done_counter):
		#	print("error occurred the initial file is" + init_counter+ "the finished task is " + done_counter)
		
		#else:
		#	print("Finished" + counter_720 +  "Video720\n")
	

def convert_video_480(inputpath):

		# if not os.path.exists('./output_videos/'):  # create output folder
		# 	os.mkdir('./output_videos/')
    
		
		outputpath = "./output_videos/"+inputpath[:-4]+"_480p.mp4"
		cmds = ['ffmpeg', '-i','./videos/'+ inputpath, '-r','30','-s','hd480',outputpath]
		conversion2 = subprocess.Popen(cmds)
		#init_counter = init_counter+1
		#counter_480 = counter_480+1

		conversion2.wait()
		print("conversion for " + inputpath +" _480 is complete" )
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
		if not os.path.exists('./output_videos/'):  # create output folder
			os.mkdir('./output_videos/')
		total_files = Vid_Q.qsize()
		#while the queue has video files run convert until nofiles left
		print("Converted " + str(total_files) + " videos!" )
		while (not Vid_Q.empty()):

			video = Vid_Q.get()

			#one thread per one resolution 

			convert_480 = threading.Thread(target=convert_video_480, args=(video,)) # convert to 480
			convert_480.start()
			convert_720 = threading.Thread(target=convert_video_720, args=(video,)) # convert to 720
			convert_720.start()

			convert_480.join()
			convert_720.join()

		print("Converted " + str(total_files) + " videos!" )

	#print(str(counter) + "files are converting in total")



def main():

	inputPath = "./videos"
	input_q = fetch_files(inputPath)


	

	# init_counter = 0
	# done_counter = 0
	# counter_480=0
	# counter_720 =0
	# outputPath_480 =''
	# outputPath_720 = ''

	#START Threading
	conversion = threading.Thread(target=Threading, args =(input_q,))

	conversion.start()




if __name__ == '__main__':
	main()

