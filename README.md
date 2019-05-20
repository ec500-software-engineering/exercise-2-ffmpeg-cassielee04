# python-ci-template
minimal template for Python Travis-CI. Prereqs installed from requirements.txt

# Introduction 
For this exercise, I use FFMPEG library to convert the video in python. Each computer has different specs of Cores. Depending  on the number of cores, the number of videos that can be converted per certain time could be decided. For my computer that has 2 Cores, 2 videos could be converted at a time. With in the FFPEG I used subprocess to convert and also test the duration. There are three files to run the program: main.py, test_duration.py. These files will run and convert the video to 720 hd and 480 hd using threading or parallel programming. After the converting, the test_duration will check if the original video and the result video has the same duration of video times.     
 
# Architecture
![Alt text](/diagram.png?raw=true "architecture")

As the diagram shows, the main.py c converts the video using threading. First the program check if the queue is empty or not. If empty, the queue stores the test video. Then the main.py calls "convert_video_720" and "convert_video_480" by threading. The programs runs asynchronously and gives the result videos parallel. In Subprocess.py, "test_files.py" is added. Here the test file tests if the converting achieved successfully. By using subprocess from ffmpeg, the test_files compares if original video's duration is the same as result video's duration. 
# Installation Needed
```python
  brew install ffmpeg
  pip install -U pytest
```

# How to run the program
```python
  python3 main.py
```
