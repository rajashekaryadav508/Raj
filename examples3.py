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
print(d,end="")
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
        pass
    
    else:
        print(i)

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
'''
'''
#11/10/2018

t=(1,2,3,4,1)
#for i in t:
    #print(it)

#print(t.index(3))
#print(t.count(1))
#print(t[3:])
t="hari",1,2
#print(type(t))
#print(t)
t1=()
#t1[0]=5 error
#print(t1)

t1=t1+(1,2,3)
#print(t1)

s={1,2,3,4,2}
#print(s[2]) error
s.add(51)
#print(s)
s1=s.copy()
#print(s1)
s1.remove(51)
print(s1)
#s1.pop(2)error
#print(s1)

l9=[1,2,3,4]
#l9.pop()
#print(l9)

s3=set()
print(type(s3))
#print(s3)
s3.add(30)
#print(s3)


s2={4,5,6,7,1,2}

print(s | s2)
print(s & s2)

l4=[1,2,3,4,1,2,3]
x=set(l4)
print(list(x))

print(2,"+",3)

#d={"k":10}
#print(d.get("k1"))
d={}
d["k1"]=100
print(d)


d2={1:100,"k2":200,3:300}
print(d2)

print(d2.items())
print(d2.keys())
print(d2.values())

'''
'''
def h():
    print("hiiiiiii")

h()

def func2():
    a=10
    b=20
    c=a+b
    print(c)


#func2()

def func2():
    a=10
    b=20
    c=a+b
    return c


#func2()

def func2(a,b):
    
    print(a+b)


#func2(10,20)

def func3(a,b):
    c=a+b
    
    return c

x=func3(40,50)
print(x)


def x ():
    print(10)
    return 20

x()
z=x()
print(z)



class hari:
    def f(self):
        #print("hiiiiiiiii")
        return 10


#print(hari().f())
#x.f()
hari().f()
x=hari().f()
#print(x)


class a:
    def assign(self,name,sal):
        self.name=name
        self.sal=sal

    def printassign(self):
        print(self.name)
        print(self.sal)




z=a()
z.assign("hari",2000)
z.printassign()


x=a()
x.assign("babu",2000)
x.printassign()


class b:
    def assign(self,name="dummy",sal=20000):
        self.name=name
        self.sal=sal

    def printassign(self):
        print(self.name)
        print(self.sal)


b1=b()
b1.assign("shekar",30000)
b1.printassign()

'''
#16/10/2018

'''
class c:
    def kk(self,name,sal):
        self.name=name
        self.sal=sal

    def assign(self):
        print(self.name)
        print(self.sal)

c1=c()
c1.kk("kk",100)
c1.assign()


a=100#global variable
def mul():
    global a
    a=10 #local variable
    print("local",a)
    print("global",a)
    #return a*a

mul()


def add():
    read_number()
    print(no1+no2)

def mul():
    read_number()
    print(no1*no2)

def read_number():
    global no1
    global no2
    no1=int(input("enter no1"))
    no2=int(input("emter no2"))

mul()


class icici:
    i_rate=10#static variable
    balance=0
    def kk(self,name,balance):#instance variables
        self.name=name
        self.balance=balance
    def printvalues(self):
        print(self.name)
        print(self.balance+balance)
        print(icici.i_rate)
        print(icici.balance)

c=icici()
c.kk("gg",20000)
c.printvalues()


class sbi:
    i_rate=5
    balance=1000
    def deposit(self,amount):
        self.balance=self.balance+amount

    def showbalance(self):
        print(self.balance)
        print(sbi.i_rate)

        
s=sbi()
s.deposit(2000)
s.showbalance()
        

k=sbi()
k.deposit(3000)
k.showbalance()


'''

'''
class x:
    def __init__(self):
        self.name="ravi"
        self.sal=10000
        #print(self.name)
        #print(self.sal)
    def display(self):
        print(self.name)
        print(self.sal)
        
x1=x()
x1.display()
y1=x()
y1.display()
'''
class z:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        #print(self.name)
        #print(self.sal)
    def display(self):
        print(self.name)
        print(self.sal)
        


#z1=z("krishna",10000)
#z1.display()


class xy:
    def __init__(self,fname="dummy",lname="dummy"):
        self.fname=fname
        self.lname=lname
        print(self.fname)
        print(self.lname)

#xy1=xy()
#xy1=xy("hari","babu")
#xy1=xy("kk")

       
fname=input("enter fname")
lname=input("enter lname")
#xy=xy(fname=fname,lname=lname)
xy=xy(lname=lname)










