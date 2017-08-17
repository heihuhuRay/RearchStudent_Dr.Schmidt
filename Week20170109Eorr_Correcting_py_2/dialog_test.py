#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *


import Tkinter as tk

dialog_dic = {
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
				 0 : "E:\StudyMaterials\TU-Chemnitz\2016WS\##RearchStudent_Mr.Schmidt\Week20161223ComninationAllFunctions\Video_0b_Nina.mp4",
				 1 : "",
				 2 : "",
				 3 : "",
				 4 : "",
				 5 : "",
				 6 : "",
				 7 : "",
			   
			 }

def create_window(button_num):
	window = tk.Toplevel(root)
	print("current_num is:",button_num)
	for next_button_num in dialog_dic[button_num]:#有时间把list改成dic
		B = tk.Button(window, text = next_button_num, command = lambda i=next_button_num : create_window(i))
		#B = tk.Button(window, text = next_button_num, command = partial(create_window, button_num))
		B.pack()
		add_to_VideoStream()
		print("next_button_num is :",next_button_num)
		
def add_to_VideoStream():
	#print("Playing the video now.")
	pass
root = tk.Tk()
b = tk.Button(root, text="START", command = lambda:create_window(0))
b.pack()

root.mainloop()