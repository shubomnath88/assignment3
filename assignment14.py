#ques1
f=open("test1.txt",encoding="utf8")
j=(f.readlines())
print(j.reverse())
n=int(input("enter no. of line"))
for i in range(0,n):
    print(j[i])
f.close()

#ques2
a="best"
f=open("test1.txt",encoding="utf8")
i=(f.readlines())
print(i.count(a))


#ques3
with open("test1.txt",encoding="utf8") as f:
    with open("test3.txt","w") as g:
        for line in f:
            g.write(line)


#ques4
f=open("test1.txt",encoding="utf8")
g=open("test3.txt",encoding="utf8")
h=open("test2.txt","a")
for l1 in f:
    h.write(str(l1)+'\t')
    print(l1)
    for l2 in g:
        h.write(str(l2)+'\t')
        print(l1)
f.close()
g.close()
h.close()


#ques5
import random
a = open("tst.txt","a")
for i in range(10):
    i=random.randint(1,100)
    a.write(str(i))
    print(i)
a.close()



