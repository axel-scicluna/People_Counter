import StreamCapture as stream
import VideoToImageConv as image
import ObjectDetection as detect
import backup as backup
import time


while True:
    #TO DO

    #Don't forget to add model in folder

    #capture video
    print("start")
    stream.main()
    #convert video
    image.main()
    #detect objects
    detect.main()
    #detects backup
    backup.main()
    #sleep for 30 min
    print("Done! sleeping for 30 min")
    time.sleep(1800)#1800 30 min
    

    #Need retinanet_resnet50_fpn_coco-eeacb38b.pth in folder to work
    #pip uninstall -y (pip freeze) uninstall pip
    #pip install -r dependencies.txt