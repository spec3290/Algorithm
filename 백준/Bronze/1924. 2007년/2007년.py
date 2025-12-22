import sys
from datetime import datetime, timedelta
date1 = datetime(2007,1,1)
day = "MON"
date = list(map(int,input().split()))
date2 = datetime(2007,date[0],date[1])

duration = (date2-date1).days
if duration%7 == 0:
    day='MON'
elif duration%7 == 1:
    day='TUE'
elif duration%7 == 2:
    day='WED'
elif duration % 7 == 3:
    day = 'THU'
elif duration%7 == 4:
    day='FRI'
elif duration%7 == 5:
    day='SAT'
elif duration%7 == 6:
    day='SUN'

print(day)