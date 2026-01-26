# Dates & Times in Python

import datetime # import datetime module

# create date object
date1 = datetime.date(2026,1,24)
print(date1) # 2026-01-24 year, month, date

#today
today = datetime.date.today()
print(today) # 2026-01-26

#time object
time = datetime.time(1,2,3) 
print(time) # 01:02:03 hours, min, sec

# now
now = datetime.datetime.now()
print(now) # 2026-01-26 15:54:00.519061

#formatting - format codes
now = now.strftime("at %H:%M:%S on %d-%m-%Y") 
print(now) # at 16:00:13 on 26-01-2026

# ------------Exercise---------------------------

target_datetime = datetime.datetime(2020,1,2,0,45,45)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed.")
else:
    print("Target date has not passed.")    
