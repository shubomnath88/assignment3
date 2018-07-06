#ques1
import numpy as np
r=np.random.randint(10,size=(10,1))
print(r.mean(axis=0))

#ques2
s=np.random.randint(20,size=(20,1))
print(np.var(s))
print(np.std(s, axis=0))

#ques3
a = np.full((10,20),8)
print(a)
b = np.full((20,25),6)
print(b)
c=np.matmul(a, b)
print(c)

#ques4
def f(i):
    return(1/(1+(np.exp(-1))))
A=np.random.rand(10,1)
print("original array = ",A)
B=f(A)
print("new array = ",B)