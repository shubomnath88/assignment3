#ques2
n = 6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
print(perfect(n))
for i in range(1,1001):
    if(perfect(i)==True):
        print(i)
#ques1
radius = float(input("enter radius"))
def area(rad):
    return 3.14*rad*rad
ar = area(radius)
print(ar)

#ques3
def mul(n,i=1):
    p = n*i
    if i==11:
        return
    print(str(n)+" x "+ str(i) +"=" + str(p))
    mul(n,i+1)
mul(int(input("enter no")))

#ques4
def power(b,e):
    if(e==1):
        return(b)
    else:
        return(b*power(b,e-1))
b = int(input("base="))
e = int(input("exponential="))
print("result=",power(b,e))
#ques5
n=int(input("enter"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print('factorial=',fact(n))

