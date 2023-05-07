import os
import shutil
from datetime import datetime

def main():
#checks if backup exists
    if os.path.isdir('Backup'):
        print("folder exists")
    else:
        print("foldes does not exist")
        os.makedirs("Backup")

    src = os.path.split(__file__)[-2]


    #loops trough images , copies them and renames them
    for x in os.listdir("Images"):
        shutil.copy2(src+"\Images\\"+x,src+"\Backup\\"+datetime.strftime(datetime.now(),"%H%M%S")+x)

    #if video exists than copy video with rename
    if os.path.exists(src+"\\recording\\captured_video.mp4"):
        shutil.copy(src+"\\recording\\captured_video.mp4",src+"\\Backup\\"+datetime.strftime(datetime.now(),"%H%M%S")+"captured_video.mp4")
        print("Recording Backed up")

if __name__ == "__main__":
    main()


