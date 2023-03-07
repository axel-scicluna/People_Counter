import cv2
import os

def main():
  # converts the video into images that the A.I can
  if os.path.isdir('Images'):
    #exists
    for path in os.listdir('Images'):
      os.remove("Images/"+path)
  else:
    #does not exist
    os.makedirs('Images')



  vidcap = cv2.VideoCapture('recording/captured_video.mp4')
  success,image = vidcap.read()
  count = 0
  skip = 0
  ImageNo = 1
  while success:
    #gets 1 frame every 10 frames
    if skip >= 60:#60 normal
      cv2.imwrite("Images/frame%d.jpg" % ImageNo, image)     # save frame as JPEG file      
      
      print('Read a new frame: ', success)
      ImageNo += 1
      skip = -1

    success,image = vidcap.read()
    skip += 1
    count += 1

  if __name__ == "__main__":
        main()