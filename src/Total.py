import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

data = pd.read_csv('data.csv')



#drops na rows
data = data.dropna()
#make sure indexes pair with number of rows
data= data.reset_index()
#drops old index
data = data.drop(["index"],axis=1)



Week = [0,0,0,0,0,0,0]
#iterates every row
for index, row in data.iterrows():
    

    result = row['Date']
    #splits date time into date
    first = result.split()
    #from y/m/d to Day
    day = datetime.datetime.strptime(first[0],'%Y-%m-%d').strftime('%A')

    #Depends what day it is adds to array
    match day:
        case 'Monday':
            Week[0] += row['People']
        case 'Tuesday':
            Week[1] += row['People']
        case 'Wednesday':
            Week[2] += row['People']
        case 'Thursday':
            Week[3] += row['People']
        case 'Friday':
            Week[4] += row['People']
        case 'Saturday':
            Week[5] += row['People']
        case 'Sunday':
            Week[6] += row['People']

  
print(Week)
columns = ['Monday',"Tuesday","Wednesday","Thursday","Friday","Saterday","Sunday"]



fig = plt.figure(figsize = (10, 5))
plt.bar(columns,Week,width=0.4)

plt.ylabel("Amount")
plt.xlabel("Day")
plt.show()
