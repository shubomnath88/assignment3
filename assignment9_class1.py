#ques1
class Circle():
    def __init__(self,radius):
        self.r=radius
    def getarea(self):
        area=3.14*self.r*self.r
        print("area=",area)
    def getcircumference(self):
        cir = 2*3.14*self.r
        print("circumference=",cir)
c=Circle(5)
c.getarea()
c.getcircumference()
#ques2
class Student():
    def __init__(self,roll,name):
        self.r=roll
        self.n=name
    def display(self):
        print("name=",self.n)
        print("roll_no=",self.r)
s=Student(20,"shubom")
s.display()
#ques3
class Temprature():
    def __init__(self,cel,far):
        self.c=cel
        self.f=far
    def convertfahrenheit(self):
        fahrenheit=(1.8*self.c)+32
        print("fahrenheit=",fahrenheit)
    def convertcelsius(self):
        celsius=(self.f-32)*(5/9)
        print("celsius=",celsius)
t=Temprature(35,108)
t.convertfahrenheit()
t.convertcelsius()
#ques4
class Moviedetails():
    movie="terminator"
    artist="arnold"
    year=1990
    rating=4.5
    def __init__(self):
        print("details are :")
    def display(self):
        print("movie name=",self.movie)
        print("artist name=",self.artist)
        print("year of release=",self.year)
        print("ratings are ",self.rating)
m=Moviedetails()
m.display()
d=Moviedetails()
d.movie="thor"
d.artist="deneal"
d.year=2011
d.rating=4.0
d.display()
#ques5
class Expenditure():
    def __init__(self,exp,sav):
        self.e=exp
        self.s=sav
    def display(self):
        print("expenditure=",self.e)
        print("savings=",self.s)
    def total(self):
        sal=self.e+self.s
        print("total salary = ",sal)
e=Expenditure(25000,15000)
e.display()
e.total()

