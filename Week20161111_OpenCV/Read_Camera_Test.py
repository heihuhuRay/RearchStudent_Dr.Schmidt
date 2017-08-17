import numpy as np
import cv2
import time

def Store_Video(cap):
	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

	while(cap.isOpened()):
	    ret, frame = cap.read()
	    if ret==True:
	        frame = cv2.flip(frame,0)

	        # write the flipped frame
	        out.write(frame)

	        cv2.imshow('frame',frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	    else:
	        break

	# Release everything if job is finished
	cap.release()
	out.release()
	cv2.destroyAllWindows()

def Play_Camera_Video(cap):
	list_frame = []
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		list_frame.append(frame)
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# Display the resulting frame
		cv2.imshow('frame',gray)
		i = i+1
		print('CV_CAP_PROP_FOURCC',cap.get(cv2.CAP_PROP_FOURCC))
		if i == 30:
			break
		#if cv2.waitKey(1) & 0xFF == ord('q'):
		#break
		cap.release()
		#cv2.waitKey(0)
		cv2.destroyAllWindows()
		# When everything done, release the capture
		print('CV_CAP_PROP_POS_FRAMES',cap.get(cv2.CAP_PROP_POS_FRAMES))
		print('CV_CAP_PROP_FPS',cap.get(cv2.CAP_PROP_FPS))
		print('CV_CAP_PROP_FRAME_WIDTH',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		print('CV_CAP_PROP_FRAME_COUNT',cap.get(cv2.CAP_PROP_FRAME_COUNT))
		#print(list_frame)

def StoreFramesIntoQueue(queue,frame_num):
	# frame_num = 30 30 frames/s
	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	for i in range(frame_num):
		queue.append(gray)
	return queue

# define Queue
class Queue(object):
    queue = []
    def __init__(self, init_list):
        self.queue = init_list
    def isEmpty(self):
        return self.queue == []
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        if self.queue:
            a=self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError('queue is empty')
    def size(self):
        return len(self.queue)
    def show_queue(self):
    	return self.queue

if __name__ == '__main__':
	#Store_Video(cap)
	q = Queue([]).show_queue()
	# delay 30 frames
	q_delay = StoreFramesIntoQueue(q,3000) 
	for f in q_delay:
		cv2.imshow('frame',f)
	# while True:
	# 	cv2.imshow('frame',q_delay.dequeue())
	# 	#print('Showing: ',q_delay.dequeue())
	# 	cap = cv2.VideoCapture(0)
	# 	ret, frame = cap.read()
	# 	#gray_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# 	q_delay.enqueue(gray_new)

############################################################################################################################################

# propId:
# 0	CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
# 1	CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# 2	CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
# 3	CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# 4	CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# 5	CV_CAP_PROP_FPS Frame rate.
# 6	CV_CAP_PROP_FOURCC 4-character code of codec.
# 7	CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# 8	CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# 9	CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# 10	CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# 11	CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# 12	CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# 13	CV_CAP_PROP_HUE Hue of the image (only for cameras).
# 14	CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# 15	CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# 16	CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# 17	CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
# 18	CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
# 19	CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
# 20	CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
# 21	CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)
