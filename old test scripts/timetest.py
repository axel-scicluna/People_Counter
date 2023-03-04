from datetime import datetime
import time
import math

myTime = datetime.now()

hour = int(myTime.strftime('%H'))
min = int(myTime.strftime('%M'))
second = int(myTime.strftime('%S'))
leftover = 0
print(datetime.now().second)
timer = 10


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
        nowSecond = int(myTime.strftime('%S'))

        if  leftover == 0:
                #no problem no left over
                if nowMin >= min+timer and nowSecond == second:
                        #ITS 10 MINUTE!
                        print(nowMin)
                        print(min)
                        print("10 minute passed with left over")
                        break
        else:
                if nowHour == hour+1 and nowMin >= leftover and nowSecond == second:
                        #ITS 10 MINUTE!
                        print("10 minute passed")
                        break
        #run the code every 10 seconds
        time.sleep(10)

        
