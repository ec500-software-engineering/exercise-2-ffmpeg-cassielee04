# python-ci-template
minimal template for Python Travis-CI. Prereqs installed from requirements.txt

# Introduction 
For this exercise, I use FFMPEG library to convert the video in python. Each computer has different specs of Cores. Depending  on the number of cores, the number of videos that can be converted per certain time could be decided. For my computer that has 2 Cores, 2 videos could be converted at a time. With in the FFPEG I used subprocess to convert and also test the duration. There are three files to run the program: main.py, Subprocess.py, and test_files.py. These files will run and convert the video to 720 hd and 480 hd using threading or parallel programming. After the converting, the test_file will check if the original video and the result video has the same duration of video times.     
 
# Architecture
![Alt text](/architecture.pdf?raw=true "architecture")
# Installation Needed
```python
  brew install ffmpeg
  pip install -U pytest
```

# How to run the program
```python
  python3 main.py
```
# Process


# Unit Test
