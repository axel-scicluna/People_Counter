import cv2
import os
from datetime import datetime

RTSP_URL = 'https://hd-auth.skylinewebcams.com/live.m3u8?a=kuve7b3gej0ik7l7ra75ov3f93'



os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp' # Use tcp instead of udp if stream is unstable

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 30

video_codec = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter('recording/captured_video.mp4', video_codec, fps, (frame_width, frame_height))

now = datetime.now().second
nowMinutes = datetime.now().min
while True:
    ret, frame = cap.read()

    if ret == True:
        video_output.write(frame)
        cv2.imshow("Video Recording", frame)
        print(datetime.now().second)
        #exists after 5 seconds or when the minute passes over
        if now+5 <= datetime.now().second or nowMinutes < datetime.now().min:
            break

    else:
        break

cap.release()
video_output.release()
cv2.destroyAllWindows()
print('Video was saved!')