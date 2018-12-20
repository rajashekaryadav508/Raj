#print("hie")
a=10
b=10
c=a/b
'''
print("the sum of a,b"+"hhhhh",c)
s="hello worrld 'hii' tjiss"
print(s)


d=20
f=30
x=d
d=f
f=x
print(d,end="") - if you want to print both the print statements in same line then use end statement, this is used in printing the pattern
print(f)
print("h")
'''
'''
a=30

b=10
print(a is not b)


n1=30
n2=20
'''
'''
if(n1>n2):
    print("n1 greater then n2")
if(n2>n1):
    print("n2 greater then n1")



n1=float(input("please enter n1 values"))
n2=float(input("please enter n2 value"))
print(n1+n2)


balance=20000
pin_no=int(input("plese enter pin no"))

if(pin_no==5475):
    print("entered pin is coorect")
    withdraw=int(input("enter withdraw amount"))
    if(withdraw%100==0 and withdraw<balance and withdraw!=0):
        balance=balance-withdraw
        print(balance)
    else:
        print("entered amount not in balance or not an multiple of hundred ")
else:
    print("ented pin is wrong")


'''

'''
import re
hip=input("enter ip")
x=re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
patt=x.match(hip)
if patt:
    print("valid")
else:
    print("invalid")
'''
'''
for x in range(10):
    print(x)
print("*********")
for y in range(1,10):
    print(y)
print("**********")
for z in range(0,10,2):
    print(z)


print("*******")
for x in range(0,10):
    if x%2==0:
        print(x)

'''
'''
i=1
while(i<10):
    print(i)
    i=i+1

i=1
while(True):
    tno=int(input("enter tno"))
    eno=int(input("enter eno"))
    for i in range(1,eno+1):
        print(tno,"*",i,tno*i)
        i=i+1
'''
'''
for x in range(5):
    if(x==2):
        break
    else:
        print(x)  
else:
    print("all values are printed")
           
i=1
while(i<10):
    if(i==5):
        break
    else:
        print(i)
        i=i+1
else:
    print("sommee")


for x in range(3):
    for y in range(1,4):
        print(y,end=" ")
    print(" ")



print("hii","hello")
print("hello")



for x in range(10,0,-1):
    print(x)

'''
'''
s="hari"
#print(s)
s[4]=1
print(s)
for i in s:
    print(i)
'''
'''
z=123
z[3]=4
print(z)
'''

l=[1,2,3,4]
#print(l)
#print(l[1])
#print(l[3])
#print(l[:])
#print(l[:3])
#print(l[2:])
#print(l[0:3:-1])
#print(l[3:0:-1])
#print(l[-1])
#print(l[::1])
#print(l[::-1])
'''
s="hari"
z=[1,2,3,4]
l=[5,6,7,8]
#l.append(2)
#l.append(z)
#l.append(s)
#print(l)


#l.extend(4)
l.extend(z)
#print(l)
#print(l)
l1=[1,2,3,4,5,6,7,8,9]
for x in l1:
    if(x%2==0):
        print(x)

'''

l3=[3,5,2,1,6,6,7,8,9]
#l3.sort()
#print(l3)
#l3.reverse()
#print(l3)
#l3.remove(9)
#print(l3)
#l3.pop(6)
#print(l3)
#print(l3.index(6))
#print(l3.count(6))
#l4=l3.copy()
#print(l4)
#l4.clear()
#print(l4)

#l1=[1,2,3,4,5,6,7,8,9]
#print(l1[0:9:2])
'''
l1=[3,4,0,5,7,6,1,2,9]

for i in range(1,11):
    if i in  l1:
        break
    
    else:
        print(i)
'''
l4=["hari","babu","raj","kumar","srinu"]
l5=["kk","jj","kumar","krishna","ll","mm"]

for x in l4:
    if x  in l5:
        print(x)

s="wonders"
print(s[::-1])
print(s[2])
s="".join(sorted(s))
print(s)
#print(sorted(s))

s="hello wolrd"

n=1234
a=str(n)
n=int(a[::-1])
print(n)
print(type(n))

print("hello")








    
