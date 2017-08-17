# -*- coding: utf-8 -*-

import Queue
import cv2
import threading
import time
import datetime
import sys

class readThread(threading.Thread):  
	cap = None
	queue_r = None
	queue_w = None
	idx = 0
	interval = 0.01
	def __init__(self,cap,queue_r,queue_w,interval):
		threading.Thread.__init__(self)
		self.cap = cap
		self.queue_r = queue_r
		self.queue_w = queue_w
		self.interval = interval
	def run(self):
		print "readThread is running now"
		while 1:
			print(str(datetime.datetime.now()) + "\treadThread:put\t" + str(self.idx))
			self.idx += 1
			ret,frame = self.cap.read()
			if ret:
				#如果读队列满了，则将最先进入队列的帧拿出来放入写队列中，再将这一帧push进去
				if self.queue_r is None:
					self.queue_w.put(frame)
				else:
					if self.queue_r.full():
						self.queue_w.put(self.queue_r.get())
					self.queue_r.put(frame)
			time.sleep(self.interval)
class writeThread(threading.Thread):
	queue = None
	interval = 0.01
	def __init__(self,queue,interval):
		threading.Thread.__init__(self)
		self.queue = queue
		self.interval = interval
	def run(self):
		print "writeThread is running now"
		while 1:
			while not self.queue.empty():
				frame = self.queue.get()
				cv2.imshow("demo",frame)
				cv2.waitKey(1)
			time.sleep(self.interval)
class camHandler(object):
	#读取摄像头的帧队列，满之后将会把溢出的内容放入写队列中去用于显示
	queue_r = None
	#显示的队列
	queue_w = None
	t_read = None
	t_write = None
	cap = None
	def __init__(self,fps=30,delay=1):
		self.cap = cv2.VideoCapture(0)
		depth = int(fps * delay)
		if 0 == depth:
			self.queue_r = None
		else:
			self.queue_r = Queue.Queue(depth)
		interval = 1.0 / fps
		self.queue_w = Queue.Queue(0)
		self.t_read = readThread(self.cap,self.queue_r,self.queue_w,interval)
		self.t_write = writeThread(self.queue_w,interval)
	def run(self):
		print "start t_read"
		self.t_read.start()
		self.t_write.start()
		self.t_read.join()
		self.t_write.join()
if __name__ == '__main__':
	print("a")
	cam = camHandler(30,0.7)
	cam.run()