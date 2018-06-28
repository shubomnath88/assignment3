#QUES1
# ZeroDivisionError

#QUES2
try:
    a=[1,2,3]
    print(a[3])
except IndexError:
    print("index not found")

#QUES3
# An exception

#QUES4
# -5
# a/b result in 0

#QUES5
try:
    a = int(input("enter integer"))
    import shubom
    b=[1,2,3]
    print(b[3])
except IndexError:
    print("index not found")
except ImportError:
    print("file not found")
except ValueError:
    print("please enter int")

#QUES6
class AgeTooSmallError(Exception):
    pass
try:
    a = int(input("enter age"))
    if(a<18):
        raise AgeTooSmallError
except AgeTooSmallError:
    print("not eligible")
else:
    print("eligible")
