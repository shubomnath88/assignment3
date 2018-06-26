#ques1
import threading
import time
import math
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread. __init__(self)
        self.h = i
    def run(self):
        time.sleep(5)
        print("value is",self.h)
thread1 = mythread(1)
thread1.start()

#ques2
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread. __init__(self)
        self.h = i
    def run(self):

        print("Numbers are",self.h)
for i in range(1,11):
    time.sleep(1)
    thread2 = mythread(i)
    thread2.start()


#ques3
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread. __init__(self)
    def run(self):
        l = ["xyz",122,23,"abd",12.8]
        for j in range(len(l)):
            time.sleep(2 * j)
            print(l[j])
thread3 = mythread()
thread3.start()


#ques4
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread. __init__(self)
    def factorial(self):
        i = int(input("enter i :-"))
        print(math.factorial(i))
thread4 = mythread()
thread4.factorial()



