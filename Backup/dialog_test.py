#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
import threading
import Queue
import Tkinter as tk
import cv2

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
				#Button : "Video Directory"
				 0 : "Video_0b_Nina.mp4",
				 1 : "Video_1_Nina.mp4",
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
	for next_button_num in dialog_dic[button_num]:
		B = tk.Button(window, text = next_button_num, command = lambda i=next_button_num : create_window(i))
		#B = tk.Button(window, text = next_button_num, command = partial(create_window, button_num))
		B.pack()
		print("next_button_num is :",next_button_num)
		
def add_to_VideoQueue(video_file_dir):
	#print("Adding frames to the queue now.")
	self_file_dir = video_file_dir
	cap = cv2.VideoCapture(self_file_dir)
	# start playing aduio thread
	thread1 = threading.Thread(target = play_Audio, args = (filename,))

	
	while(cap.isOpened()):
	    ret, frame = cap.read()

	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

def play_Audio(audio_file_dir):
	pass
##########################################################################################

##########################################################################################

# Create new threads
thread1 = threading.Thread(target = play_Audio, args = (filename,))
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

root = tk.Tk()
b = tk.Button(root, text="START", command = lambda:create_window(0))
b.pack()

root.mainloop()