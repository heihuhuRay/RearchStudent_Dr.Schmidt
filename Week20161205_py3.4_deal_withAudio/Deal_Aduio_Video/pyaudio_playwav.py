import pyaudio
import wave
import sys
# Voice Detection
#import pyaudio
import wave
# GUI
import Tkinter
from Tkinter import *
import Tkinter as tkinter
# Video Stream Delay
import Queue
import cv2
# Multiple threads
import threading
import time
import datetime
import sys
#################################################################################################
#################################################################################################
global_delay = 0
list_frame = []
def playVideo(File_Name_Video):
	self_File_Name_Video = File_Name_Video
	cap = cv2.VideoCapture(self_File_Name_Video)#self_File_Name_Video#()
	thread1 = threading.Thread(target = play_wav, args = ('Video_1_Nina.wav',))
	thread1.start()
	while(cap.isOpened()):
	    ret, frame = cap.read()
	    list_frame.append(frame)
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
	#play_wav('a2002011001-e02.wav')



#################################################################################################
#################################################################################################
def setDelay(Delay):
	global_delay = Delay
#################################################################################################
#################################################################################################
def showVideo(filename):
	pass




##################################################################################
def play_wav(w_f):
	CHUNK = 1024
	wf = wave.open(w_f, 'rb')
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

# building GUI
top = tkinter.Tk()
# Code to add widgets will go here...
B_Video_1 = tkinter.Button(top, text ="Video_1", command = lambda:playVideo('Video_0b_Nina.mp4'))# Using lambda here because, command = function_name, not command = function("data_1, data_2")
B_Video_2 = tkinter.Button(top, text ="Video_2", command = lambda:playVideo('Video_1_Nina.mp4'))
B_Delay_1s= tkinter.Button(top, text ="1 Second", command = lambda:setDelay(1))
B_Delay_2s= tkinter.Button(top, text ="2 Seconds", command = lambda:setDelay(2))
B_Video_1.pack()
B_Video_2.pack()
B_Delay_1s.pack()
B_Delay_2s.pack()
top.mainloop() 