#QUES1
class Animal():
    def animal_attribute(self):
        print("there are two types of animal:- wild & domestic animal")
class Tiger(Animal):
    def tiger_attr(self):
        print("tiger is a wild animal")
t = Tiger()
t.animal_attribute()
t.tiger_attr()



#QUES2
print("AB,AB")



#QUES3
class Cops():
    def __int__(self,name,age,work,experience,designation):
        self.n = name
        self.a = age
        self.w = work
        self.e = experience
        self.d = designation
    def add(self):
        self.n = "abahy"
        self.a = 25
        self.w = "officer"
        self.e = 5
        self.d = "inspector"
    def display(self):
        print("name = ",self.n)
        print("age = ",self.a," years")
        print("work = ",self.w)
        print("experience = ",self.e," years")
        print("designation = ",self.d)
    def update(self):
        print("after updated:-")
        self.n = "raj"
        print("name = ",self.n)
        self.a = 35
        print("age = ",self.a," years")
        self.w = "officer"
        print("work = ",self.w)
        self.e = 16
        print("experience = ",self.e," years")
        self.d = "DSP"
        print("designation = ",self.d)
class Mission(Cops):
    def add_mission_details(self):
        print("details fof officers are:-")

m = Mission()
m.add_mission_details()
m.add()
m.display()
m.update()




#QUES4
class Shape():
    length = float(input("enter length "))
    breadth = float(input("enter breadth "))
class Rectangle(Shape):
    def rarea(self):
        area = self.length*self.breadth
        print("area of rectangle = ",area,"cm^2")
class Square(Shape):
    def sarea(self):
        area = self.length*self.length
        print("area of squqre = ",area,"cm^2")
r = Rectangle()
s = Square()
r.rarea()
s.sarea()






