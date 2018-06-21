#ques3
import datetime
d = datetime.date.today()
print(d.day)
#ques4
import datetime
d = datetime.date.today()
print(d.month)
#ques5
import datetime,time
d=datetime.date(1996,4,9)
print(d.day)

#ques2
import datetime,time
print(time.asctime(time.gmtime()))

#ques6
import datetime,time
print(time.asctime(time.localtime()))

#ques7
import math
print(math.factorial(7))

#ques8
import math
print(math.gcd(5,3))

#ques9
import os
print(os.getcwd())
print(os.environ)

#ques1
print("we represent time in a way that's easy to understand , python stores it in a tuple & those tuples are:")
print("index   field          value")
print(" 0      years          1995")
print(" 1      month          1 to 12")
print(" 2      days           1 to 31")
print(" 3      hour           0 to 23")
print(" 4      minutes        0 to 59")
print(" 5      seconds        0 to 61")
print(" 6      day of week    0 to 6")
print(" 7      day of year    1 to 366")
print(" 8      DST            (-1,0,1)")
