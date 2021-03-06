import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

# Our operations on the frame come here
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#time.sleep(1)
# Display the resulting frame
cv2.imshow('frame',gray)
time.sleep(1)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    time.sleep(1)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()