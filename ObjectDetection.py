from imageai.Detection import ObjectDetection
from datetime import datetime
import os
import json



src = str(os.path.split(__file__)[-2])

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(src+"\\retinanet_resnet50_fpn_coco-eeacb38b.pth")
detector.loadModel()
#stores the amount of people counted for each picture
ImageArray = []
imageCount = 0 
#check the 3 picture gathered

# folder path

imageCount = 0
# Iterate directory

for path in os.listdir(src+"\\Images"):
    # check if current path is a file
    if os.path.isfile(os.path.join(src+"\\Images", path)):
        imageCount += 1
print('File count:', imageCount)


for x in range(imageCount+1):
    imageCount = 0
    if(x > 0):

        detections = detector.detectObjectsFromImage(input_image= src+"\\Images\\frame"+str(x)+".jpg" , output_image_path= src+"\\Images\\imagenew"+str(x)+".jpg", minimum_percentage_probability=30)
        
        for y in detections:
            #checks if its type person since I cant use custom objects
            if(y["name"]== "person"):
                imageCount = imageCount +1

        # Adds counted person to outside array
        ImageArray.append(imageCount)
        imageCount = 0
print(str(ImageArray))


#Re using imageCount to see biggest number
imageCount = 0
#Checks the most people counted in the picture
for z in ImageArray:
    if z > imageCount:
        imageCount = z

print("Biggest Number is: "+str(imageCount))

with open('data.txt', 'a') as f:
    f.write('\nDate:'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"|People:"+str(imageCount))
#TO DO 
# REMOVE RECIEVED IMAGE DON'T NEED IT
# LOOP CODE EVERY X AMOUNT OF SECONDS
#get stream key when the key breaks
#remove old videos and image before loop



