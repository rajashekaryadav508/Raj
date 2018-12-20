import re
s="haribabu"
#x=re.split("b",s)
x=re.split("b",s,1)
#print(x)


h="programming java hari from java python as so popular"
#z=re.sub("java","python",h)
#print(z)


'''
#print(h.replace("java","python"))
x=re.match("java",h)
#print(x)
y=re.search("python",h)
#print(y)

a=re.findall("java",h)
print(a)


b="krishnaram"
#c=re.findall(r"\w",b)
#c=re.findall("\w\w",b)
#c=re.findall("\w{2}",b)
#c=re.findall("\w$",b)
#c=re.findall("^\w",b)
c=re.findall("\w+",b)
print(c)
for x in c:
    
    
    z1="".join(str(x))
print(z1)
print(type(z1))

'''


s="kkr123456sskmm124789"
s1=re.findall("\d{2}",s)
print(s1)
l=[]
for x1 in s1:
    y1=int(x1)
    z1=l.append(y1)

print(l)
print(sum(l))

q="hbdasdsk1234bjJHYTRhsd12356"

#a1=re.findall("[a-z]",q)
#a1=re.findall("[a-zA-Z]",q)
#print(a1)
'''
def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True
        

validIP(133.225.8.124)
'''
