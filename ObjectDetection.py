from imageai.Detection import ObjectDetection
import os


src = str(os.path.split(__file__)[-2])

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(src+"\\retinanet_resnet50_fpn_coco-eeacb38b.pth")
detector.loadModel()
#stores the amount of people counted for each picture
ImageArray = []
imageCount = 0
#check the 3 picture gathered
for x in range(4):
   
    if(x > 0):

        detections = detector.detectObjectsFromImage(input_image= src+"\\Images\\"+str(x)+".png" , output_image_path= src+"\\Images\\imagenew"+str(x)+".jpg", minimum_percentage_probability=30)
        
        for y in detections:
            #checks if its type person since I cant use custom objects
            if(y["name"]== "person"):
                imageCount = imageCount +1

        # Adds counted person to outside array
        ImageArray.append(imageCount)
        imageCount = 0
print(str(ImageArray[0])+" :1 | "+str(ImageArray[1])+" :2 | "+str(ImageArray[2])+" :3 | ")

#Re using imageCount to see biggest number
imageCount = 0
#Checks the most people counted in the picture
for z in ImageArray:
    if z > imageCount:
        imageCount = z

print("Biggest Number is: "+str(imageCount))

#TO DO 
# ADD AUTO CAPTURE FROM WEBSITE
# REMOVE RECIEVED IMAGE DON'T NEED IT
# STORE BIGGEST NUMBER IN A NOTEPAD
# LOOP CODE EVERY X AMOUNT OF SECONDS


