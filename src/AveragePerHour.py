import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime


data = pd.read_csv('data.csv')

#function to avoid additional case in each day so just return which bucket to put the value into
def dayConvert(weekDay):
        match weekDay:
            case 'Monday':
                return 0
            case 'Tuesday':
                return 1
            case 'Wednesday':
                return 2
            case 'Thursday':
                return 3
            case 'Friday':
                return 4
            case 'Saturday':
                return 5
            case 'Sunday':
                return 6

# one bucket for every hour could use 2d array maybe
day = [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]
dayCount = [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]
#drops na rows
data = data.dropna()
#make sure indexes pair with number of rows
data= data.reset_index()
#drops old index
data = data.drop(["index"],axis=1)

#ctrl + [ REMOVE TABBING


for index, row in data.iterrows():

    result = row['Date']
    #splits date time into date
    first = result.split()
    #from y/m/d to Day
    hour = datetime.datetime.strptime(first[1],'%H:%M:%S.%f').strftime('%H')
    weekday = datetime.datetime.strptime(first[0],'%Y-%m-%d').strftime('%A')


    #get day
    #count hourly person count to day
    #0,0 [Monday,9am],0,1 [Monday,10am],1,0 [Tuesday,9am]
    match hour:
        case '09':
            day[dayConvert(weekday)][0] += row['People']
            dayCount[dayConvert(weekday)][0] += 1
        case '10':
            day[dayConvert(weekday)][1] += row['People']
            dayCount[dayConvert(weekday)][1] += 1
        case '11':
            day[dayConvert(weekday)][2] += row['People']
            dayCount[dayConvert(weekday)][2] += 1
        case '12':
            day[dayConvert(weekday)][3] += row['People']
            dayCount[dayConvert(weekday)][3] += 1
        case '13':
            day[dayConvert(weekday)][4] += row['People']
            dayCount[dayConvert(weekday)][4] += 1
        case '14':
            day[dayConvert(weekday)][5] += row['People']
            dayCount[dayConvert(weekday)][5] += 1
        case '15':
            day[dayConvert(weekday)][6] += row['People']
            dayCount[dayConvert(weekday)][6] += 1
        case '16':
            day[dayConvert(weekday)][7] += row['People']
            dayCount[dayConvert(weekday)][7] += 1
        case '17':
            day[dayConvert(weekday)][8] += row['People']
            dayCount[dayConvert(weekday)][8] += 1

for week in range(7):
    for timeRange in range(9):
        if day[week][timeRange] != 0:
            day[week][timeRange] = day[week][timeRange]/dayCount[week][timeRange]

columns = ['9 Am',"10 Am","11 Am","12 Am","1 Pm","2 Pm","3 Pm",'4 Pm','5 Pm']
 
fig, axs = plt.subplots(7,figsize = (12, 7),layout='constrained')
fig.suptitle('Weekly Average Per Hour')
axs[0].bar(columns,day[0],width=0.8)
axs[0].set_title("Monday")
axs[1].bar(columns,day[1],width=0.8)
axs[1].set_title("Tuesday")
axs[2].bar(columns,day[2],width=0.8)
axs[2].set_title("Wednesday")
axs[3].bar(columns,day[3],width=0.8)
axs[3].set_title("Thursday")
axs[4].bar(columns,day[4],width=0.8)
axs[4].set_title("Friday")
axs[5].bar(columns,day[5],width=0.8)
axs[5].set_title("Saturday")
axs[6].bar(columns,day[6],width=0.8)
axs[6].set_title("Sunday")

plt.show()