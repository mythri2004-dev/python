#dice code
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid option")'''

#calendar module
'''import calendar
year=2026
month=8
print(calendar.calendar(year))'''


'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter the month"))
print(calendar.month(a,b))'''


#date
'''from datetime import date
a=date.today()
print(a)

import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''
#task
'''import random
import time
for i in range(10):
    print(random.randint(0,10))
    time.sleep(2)'''
#task
'''import random
import time
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)'''

#error handling
#syntax error
'''for i in range(10):
   print(i)'''

#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''#10//0->zero division error

#logical error
'''a=10
b=20
if a<b:
    print("less")'''

'''a=10
b=20
if a>b:
    print("true")''' #not visible
    





 


