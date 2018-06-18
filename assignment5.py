#ques1
y = int(input("enter yera"))
if (y%4==0):
    print("year is leap year")
else:
    print("is not leap year")
#ques2
l = int(input("lenght"))
b = int(input("breadth"))
if(l==b):
    print("is square")
else:
    print("is rect")
#ques3
x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
if(x>y):
    if(y>z):
        if(x>z):
            print("z is youngest")
        else:
            pass
    else:
        print("y is youngest")
else:
    print("x is youngest")
if(x<y):
    if(y<z):
        if(x<z):
            print("z is oldest ")
        else:
            pass
    else:
        print("y is oldest")
else:
    print("x is oldest")
#ques4
p = int(input("enter point : "))
if(p<=50):
    print("sorry no prizes")
elif(p>50 and p<=150):
    print("wooden dog")
elif(p>150 and p<=180):
    print("book")
elif(p>180 and p<=200):
    print("chocolates")
else:
    print("wrong points")
#ques5
c = 100
p = int(input("no. of product="))
q = c*p
print(q)
if(q>=1000):
    print("with 10% discount price is " +str(q-(q/10)))
else:
    print("no discounts")
