
import time, datetime


def getDayofWeek():
#gets all the date/time information for recording the information 
    num_of_week = datetime.datetime.today().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days[num_of_week]
    return day_of_week



def getTimeStamp():
    ts = time.time()
    time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return time_stamp
