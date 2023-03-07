import StreamCapture as stream
import VideoToImageConv as image
import ObjectDetection as detect
import time

while True:
    #TO DO 
    #1. Add global variables in this file for video length and images/frames
    #2. Add more solid code try catches and other exceptions
    #3. Add Average Graph file

    #Don't forget to add model in folder

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
    

    #Need retinanet_resnet50_fpn_coco-eeacb38b.pth in folder to work
    #pip uninstall -y (pip freeze) uninstall pip
    #pip install -r dependencies.txt