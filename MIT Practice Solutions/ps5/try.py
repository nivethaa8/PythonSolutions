from datetime import datetime

# now = datetime.now() # current date and time
now = datetime(2016, 10, 12, 23, 59, 59)
print(now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%b")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m %b %Y, %H:%M:%S")
print("date and time:",date_time)