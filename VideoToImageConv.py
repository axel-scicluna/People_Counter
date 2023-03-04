import cv2
import os


for path in os.listdir('Images'):
    os.remove("Images/"+path)


vidcap = cv2.VideoCapture('recording/captured_video.mp4')
success,image = vidcap.read()
count = 0
skip = 0
ImageNo = 1
while success:
  #gets 1 frame every 10 frames
  if skip >= 10:
    cv2.imwrite("Images/frame%d.jpg" % ImageNo, image)     # save frame as JPEG file      
    
    print('Read a new frame: ', success)
    ImageNo += 1
    skip = -1

  success,image = vidcap.read()
  skip += 1
  count += 1