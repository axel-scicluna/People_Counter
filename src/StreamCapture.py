import cv2
import os
import getaddress
from datetime import datetime


#gets video capture of the stream into a folder
def main():
        
        if os.path.isdir('recording'):
                #exists
                if os.path.exists('recording/captured_video.mp4'):
                        os.remove('recording/captured_video.mp4')
        else:
                #does not exist
                os.makedirs('recording')

        


        #link below is of cam needed
        RTSP_URL = getaddress.getAddress("https://www.skylinewebcams.com/en/webcam/italia/liguria/imperia/festival-sanremo-ariston.html")

        print(RTSP_URL)



        os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp' # Use tcp instead of udp if stream is unstable

        cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

        if not cap.isOpened():
                print('Cannot open RTSP stream')
                exit(-1)

        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = 30# 15 for real world speed, 30 for x 2 speed 10 min of footage ~ 4:10 min loss of 40-45 seconds

        video_codec = cv2.VideoWriter_fourcc(*'XVID')
        video_output = cv2.VideoWriter('recording/captured_video.mp4', video_codec, fps, (frame_width, frame_height))

        myTime = datetime.now()

        hour = int(myTime.strftime('%H'))
        min = int(myTime.strftime('%M'))
        leftover = 0

        timer = 1# 3 min x 4 rotations = 12 minutes was 10
        if min+timer <= 60:
        # less than 59 or equal than no problem
                print("no more")
        else:
        #more then one hour so left over
                leftover = 60 - min

        while True:
                myTime = datetime.now()
                nowHour = int(myTime.strftime('%H'))
                nowMin = int(myTime.strftime('%M'))
                ret, frame = cap.read()

                if ret == True:
                        
                        video_output.write(frame)
                        cv2.imshow("Video Recording", frame)
                        #exists after 5 seconds or when the minute passes over

                        if  leftover == 0:
                                #no problem no left over
                                if nowMin >= min+timer:
                                        print("10 minute passed with left over")
                                        print(min)
                                        print(timer)
                                        print(nowMin)
                                        break
                        else:
                                if nowHour == hour+1 and nowMin >= leftover:
                                        #ITS 10 MINUTE!
                                        print(min)
                                        print(timer)
                                        print(nowMin)
                                        print("10 minute passed")
                                        break
                else:
                        break


        


        cap.release()
        video_output.release()
        cv2.destroyAllWindows()
        print('Video was saved!')

if __name__ == "__main__":
        main()