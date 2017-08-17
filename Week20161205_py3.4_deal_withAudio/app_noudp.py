# -*- coding: utf-8 -*-
import cv2
import datetime
class demo(object):
	#缓存队列的长度，越长延时时间越长，大概30为1s
	depth = 100
	queue = []
	cursor = 0
	is_queue_full = 0
	idx = 0
	capture = None
	def __init__(self,depth=100):
		self.capture = cv2.VideoCapture(0)
		self.depth = depth
	def frame_update(self):
		#从缓存中取出帧用于显示
		frame = self.quene_get()
		if None != frame:
			self.display_frame(frame)
		#从摄像头获取新的帧更新到缓存中去
		frame_new = self.get_frame()
		self.quene_update(frame_new)
		
	def get_frame(self):
		ret,frame = self.capture.read()
		return frame
	def display_frame(self,frame):
		cv2.imshow("demo",frame)
		cv2.waitKey(1)
		pass
	def quene_update(self,frame):
		if 0 == self.is_queue_full: # queue not full
			self.queue.append(frame)
			if len(self.queue) == self.depth:
				self.is_queue_full = 1
		else: #queue is full
			self.queue[self.cursor] = frame
			self.cursor += 1  # No idea why need +1
			if self.cursor >= len(self.queue):
				self.cursor = 0 # can replace these part by removing the first element
	def quene_get(self):
		if 0 == self.is_queue_full:
			return None
		else:
			return self.queue[self.cursor]
	def view(self):
		print(self.queue)

if __name__ == '__main__':
	stream = demo()
	while 1:
		stream.frame_update()
		