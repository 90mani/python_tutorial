#display current date and time 

import datetime
now = datetime.datetime.now()
print("current date and time :")
print(now.strftime("%d-%m-%Y %H:%M:%S"))