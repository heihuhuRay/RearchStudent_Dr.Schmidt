#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
import threading
import Queue
import Tkinter as tk
import cv2
import pyaudio
import wave

###########################################################################################################
# Queue
frame_Q = Queue.Queue(maxsize = 0) # maxsize < 1 means: no limit for the length of the queue
###########################################################################################################
dialog_dic = {
				#Button num : [next button nums]
				 0 : [1],# 假如是1，2，3
				 1 : [2,3],   # 2,3 分开
				 2 : [3],
				 3 : [4, 5, 6],
				 4 : [7],
				 5 : [7],
				 6 : [8],
				 7 : [8],
			   
			 }

Video_dir_dic = {
				#Button : "Video Directory"  .mp4
				 0 : "Video_0b_Nina.mp4",
				 1 : "Video_1_Nina.mp4",
				 2 : "Video_2_Nina.mp4",
				 3 : "",
				 4 : "",
				 5 : "",
				 6 : "",
				 7 : "",
			   
			 }

Audio_dir_dic = {
				#Button : "Audio Directory"  .wav 
				 0 : "a2002011001-e02.wav",
				 1 : "Kurzweil-K2000-Big-Mono-Bass-C1.wav",
				 2 : "Video_2_Nina.mp4",
				 3 : "",
				 4 : "",
				 5 : "",
				 6 : "",
				 7 : "",
			   
			 }
def Button_press():
	create_window()
	add_to_VideoQueue()
	play_Audio()

def create_window(button_num):
	window = tk.Toplevel(root)
	print("current_num is:", button_num)
	# start playing aduio thread
	thread1 = threading.Thread(target = play_Audio, args = (Audio_dir_dic[button_num],))
	thread1.start()
	# put frames into queue
	print("starting adding to queue")
	add_to_VideoQueue(Video_dir_dic[button_num])
	print("finish adding to queue")
	for next_button_num in dialog_dic[button_num]:
		B = tk.Button(window, text = next_button_num, command = lambda i=next_button_num : create_window(i))
		#B = tk.Button(window, text = next_button_num, command = partial(create_window, button_num))
		B.pack()
		print("next_button_num is :",next_button_num)
		
def add_to_VideoQueue(video_file_dir):
	#print("Adding frames to the queue now.")
	self_file_dir = video_file_dir
	cap = cv2.VideoCapture(self_file_dir)
	while(cap.isOpened()):
	    ret, frame = cap.read()
	    frame_Q.put(frame)
	    print("adding.....frames")
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
	print("done with storing frames")
	cap.release()

def play_Audio(audio_file_dir):
	CHUNK = 1024
	wf = wave.open(audio_file_dir, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)
	data = wf.readframes(CHUNK)
	while data != '':
	    stream.write(data)
	    data = wf.readframes(CHUNK)
	stream.stop_stream()
	stream.close()
	p.terminate()
##########################################################################################

##########################################################################################


root = tk.Tk()
b = tk.Button(root, text="START", command = lambda:create_window(0))
b.pack()

root.mainloop()