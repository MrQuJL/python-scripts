from datetime import datetime

#now = datetime.now()

#print(now)

#print(type(now))

dt = datetime(2018, 5, 28, 9, 48)
#print(dt)

t = dt.timestamp()
#print(t)

#print(datetime.fromtimestamp(t))
#print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2018-5-28 9:52:10', '%Y-%m-%d %H:%M:%S')
#print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))#星期几，月，日


















