import pandas as pd
import datetime
import time
startdate = "10/10/2018"
my_date = pd.to_datetime(startdate)
print(my_date.strftime("%Y-%m-%d"))
#actual
my_date = datetime.datetime.now()
print(my_date.strftime("%Y-%m-%d"))
#day+5
enddate = my_date + pd.DateOffset(days=5)
print(enddate.strftime("%Y-%m-%d"))
#day -5
enddate = my_date - pd.DateOffset(days=5)
print(enddate.strftime("%Y-%m-%d"))
#numeric date
print("Unix Timestamp: ", (time.mktime(my_date.timetuple())))