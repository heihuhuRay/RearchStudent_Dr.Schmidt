from sys import byteorder
from array import array
from struct import pack
# Voice Detection
import pyaudio
import wave
# GUI
import tkinter
from tkinter import messagebox
# Video Stream Delay
import queue
import cv2
# Multiple threads
import threading
import time
import datetime
import sys
#################################################################################################
#################################################################################################
global_delay = 0
def playVideo(File_Name_Video):
	self_File_Name_Video = File_Name_Video
	cap = cv2.VideoCapture(self_File_Name_Video)#self_File_Name_Video#()

	while(cap.isOpened()):
	    ret, frame = cap.read()

	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
#################################################################################################
#################################################################################################
def setDelay(Delay):
	global_delay = Delay
#################################################################################################
#################################################################################################
def showVideo(filename):
	pass


# building GUI
top = tkinter.Tk()
# Code to add widgets will go here...
B_Video_1 = tkinter.Button(top, text ="Video_1", command = lambda:playVideo('Video_0b_Nina.mp4'))# Using lambda here because, command = function_name, not command = function("data_1, data_2")
B_Video_2 = tkinter.Button(top, text ="Video_2", command = playVideo)
B_Delay_1s= tkinter.Button(top, text ="1 Second", command = lambda:setDelay(1))
B_Delay_2s= tkinter.Button(top, text ="2 Seconds", command = lambda:setDelay(2))
B_Video_1.pack()
B_Video_2.pack()
B_Delay_1s.pack()
B_Delay_2s.pack()
top.mainloop() 



