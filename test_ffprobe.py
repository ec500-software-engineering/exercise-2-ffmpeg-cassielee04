from pytest import approx
import json
import subprocess
from pathlib import Path


# def ffprobe(file:Path)->dict:
# 	input_info = subprocess.check_output(['ffprobe', '-v', 'warning',
#                                     '-print_format', 'json',
#                                     '-show_streams',
#                                     '-show_format',
#                                     file],universal_newlines=True)
# 	input_data = json.loads(input_info)
# 	return input_data


def test_duration():


	orig_vid = './videos/full_ball.mp4'
	convert_480 = './output_videos/full_ball_480p.mp4'
	#convert_720 = './output_videos/full_ball_720p.mp4'


	orig_probe = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    orig_vid],universal_newlines=True))
	probe_480 = json.loads(subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    convert_480],universal_newlines=True))
	#probe_720 = ffprobe(convert_720)

	ori_duration = float(orig_probe['streams'][0]['duration'])
	duration_480 = float(probe_480['streams'][0]['duration'])
	#duration_720 = float(probe_720['streams'][0]['duration'])

	assert ori_duration == approx(duration_480)
	#assert ori_duration == approx(duration_720)


	if __name__ == '__main__':
		test_duration()