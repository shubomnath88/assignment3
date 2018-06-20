#ques1
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11):
    print(i)

#ques2
while("true"):
    print("hii")
    break
#ques3
l = [1,2,3,4]
for i in range(len(l)):
    print(l[i]*l[i])

#ques4
a = input("entr")
l = []
print(l.append(a))
for i in range(len(l)):
    x = []
    y = []
    z = []
    if isinstance(l,int)==True:
        print(x.append(l))
        print("int=",x)
    elif isinstance(l,float)==True:
        print(y.append(l))
        print("float=",y)
    elif(isinstance(l,str)==True):
        print(z.append(l))
        print("string=",z)
    else:
        pass
    print(l)


#ques5
a=[]
for i in range(1,101):
    print(a.append(i))
    e = []
    o = []
    if(i%2==0):
        print(e.append(i))
        print("even=",e)
    else:
        print(o.append(i))
        print("odd=",o)

#ques6
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()

#ques7
a = {'name':'xyz','age':25}
for i in a:
    print(i)

#ques8
l = [1,3,8,'sd',2.5]
a = input("enter element ")
for i in range(len(l)):
    if(l[i] == a):
        print(l.pop(l[i]))
        print(l)
    else:
        print("not found")
