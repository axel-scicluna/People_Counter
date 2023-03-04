import StreamCapture as stream
import VideoToImageConv as image
import ObjectDetection as detect
import time

while True:
    #capture video
    print("start")
    stream.main()
    #convert video
    image.main()
    #detect objects
    detect.main()
    #sleep for 30 min
    print("Done! sleeping for 30 min")
    time.sleep(1800)#1800 30 min
    