import numpy as np
import cv2
import pyaudio
import time

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
