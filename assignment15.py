#ques1
import re
email="zuck26@facebook.com"\
    "page23@google.com"\
    "jeff42@amazon.com"
pattern=(r'(\w+)@([{a-z0-9})\.([a-z]{2,4})')
print(re.findall(pattern,email,flags=re.IGNORECASE))


#ques2
def getword(text,letter):
    regx = (r'[\w]*'+letter+r'[\w]*')
    return (re.findall(regx,text,re.I))

t = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
result=getword(t,"b")
print(result)

#ques3
str = "A , very very ; irregular_sentence"
print("".join(re.split('[;,\s_]+', str)))