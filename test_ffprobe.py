from pytest import approx
import main

def test_ffprobe():


	orig_vid = './videos/full_ball.mp4'
	convert_480 = './output_videos/full_ball_480p.mp4'
	convert_720 = './output_videos/full_ball_720p.mp4'


	orig_probe = main.ffprobe(orig_vid)
	probe_480 = main.ffprobe(convert_480)
	probe_720 = main.ffprobe(convert_720)

	ori_duration = float(orig_probe['streams'][0]['duration'])
	duration_480 = float(probe_480['streams'][0]['duration'])
	duration_720 = float(probe_720['streams'][0]['duration'])

	assert ori_duration == approx(duration_480)
	assert ori_duration == approx(duration_720)


	if __name__ == '__main__':
		test_ffprobe()