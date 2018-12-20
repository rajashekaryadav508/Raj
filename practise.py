'''
a=10
b=20
c=a+b
print("sum of a+b is"+"hhhh",c)
print("sum"+"Of"+"a+b"+"is"+"c")

d=20
f=30
x=d
d=f
f=x
print(d,f)

s="hello world"
print(s)

a=10
b=20
print(a is not b)

n1=20.4
n2=30.3
if(n1>n2):
    print("n1 is greater than n2")
if(n2>n1):
    print("n2 is greater than n1")


balance=10000
pin_no=int(input("Enter pin number"))
if(pin_no==1234):
    print("Entered pin is correct")
    withdraw=int(input("Enter the amount to withdraw"))
    if(withdraw<balance and withdraw%100==0 and withdraw!=0):
        balance=balance-withdraw
        print(balance)
    else:
        print("withdraw amount is incorrect")
else:
    print("entered pin is incorrect")
    
'''
'''
import re
hip=input("enter ip")
#yip=hip.split(".")
#if len(yip)!=4:
x=re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
patt=x.match(hip)
    print("Invalid")
else:
    print("valid")
'''

    
'''for x in range(10):
   print(x)
for x in range(1,10):
    print(x)
'''
'''
for z in range(1,10,3):
    print(z)

for x in range(1,10):
    if(x%3==0):
        print(x)
'''
'''
i=1
while(i<10):
    print(i)
    i=i+1
print("*********")

i=1
while(True):
    tno=int(input("Enter tno"))
    eno=int(input("Enter eno"))
    for i in range(1, eno+1):
        print(tno,"*",i,tno*i)
        i=i+1
    ans=int(input("enter 1"))
    if(ans==1):
        continue
    else:
        break
print("****")
'''
'''
for x in range(5):
    if(x==2):
     print(x)
    else:
        print("hi")
'''
'''
for x in range(5):
    if(x==2):
        break
    else:
        print(x)
else:
    print("All the values are printed")

print("*********")
i=1
while(i<10):
    if(i==5):
        break
    else:
        print(i)
        i=i+1
else:
    Print("Something")

print("**********")
'''
'''
for x in range(3):
    for y in range(4):
        print(x,end=" ")
    print(" ")
'''
'''
print("*******")
for x in range(3):
    print(x,end=" ")
'''
'''for printing the numbers in reverse order below is the syntax
'''
'''
for x in range(10,1,-1):
    print(x)
'''
'''
s="raja"
print(s)
for i in s:
    print(i)

z=123
a=str(z)
for i in a:
    print(i)
'''
l=[1,2,3,4]
#print(l)
#print(l[0])
#print(l[3])
#print(l[:])
#print(l[:1])
#print(l[:3])
#print(l[2:])
#print(l[0:3:])
#print(l[0:3:1])
#print(l[3:0:-1])
#print(l[::-1])

s="rajashekar"
z=[1,2,3,4]
l=[5,6,7,8]
#l.append(z)
#print(l)
#l.append(2)
#print(l)
#l.extend(z)
#print(l)
#b="sathya"
#l.append(b)
#print(l)
#l.extend(b)
#print(l)

#As number is not iterable extend will not work in list,but append will work,
#where as string is iterable so extend will now work in list by seperating it but
#append will still add it as a single element.Above is the example.
'''
l1=[1,3,4,6,7,8,9]
for x in l1:
    if(x%2==0):
        print(x)
for x in range(10):
    if (x%2==0):
        print(x)

l3=[3,5,2,1,6,6,7,8,9]
l3.sort()
'''
#print(l3)
#l3.reverse()
#print(l3)
#l3.remove(1)
#for remove we have to pass the value but not index
#print(l3)
#l3.pop()
#print(l3)
#for pop we dont have to mention any value, it will remove the last value in the list without sorting.
#if you pass the value it will remove that value
#l4=l3.copy()
#print(l4)
#print(l4.index(2))
#to find the index position of that number that is given as input.
#print(l4.count(6))
#used to count the number of times that number is repeated.
#print(len(l4))
#used to count the length of that list
#l4.clear()
#print(l4)
'''
l2=[3,4,0,5,7,6,1,2,9]
for i in range(1,11):
    if i in l2:
        pass
    else:
        print(i)
'''
'''
l4=["hari","babu","raj","kumar","srinu"]
l5=["kk","jj","kumar","krishna","ll","mm"]
for x in l4:
    if x in l5:
        print(x)
'''
'''
s="wonders"
print(s[::-1])
#l1=[1,2,3,4]
#print(l1[::-1])
print(s[2])
#as number is not iterable we cannot find the index position where as
#string is iterable so we can find the index position as well as reverse it.
s="".join(sorted(s))
print(s)
print(sorted(s))
'''
#s="wonders"
#print(s[::-1])
#for x in s:
#    print(x)
#s="".join(sorted(s))
#print(s)
#print(s[2])
#print(sorted(s))
#n=1234
#print(n[2])- will give error because it is not itterable
#p=str(n)
#print(p[::-1])
#n=int(p)
#print(type(n))
#print("**************")
############################tuple#############################
t=(1,2,3,4,1)
#for i in t:
#    print(i)
#print(t.index(3))
#print(t.count(1))
#print(t[:3])
#print(t[3:])
'''t="hari",1,2
t3="hari"
t4="hari",

#for a tuple we cannot give the tuple with a single element, if we are going
#to give a single element for tuple then it should be given along with comma.
print(type(t3))
print(type(t4))
'''
#If brackets are given to tuple then it is called unpacking
#If brackets are given to tuple then it is called packing
#print(type(t))
#print(t)
'''t1=(3,4,5)
t2=t1+t
#we can add two tuples using a + opperand but not in set, for set it should be
#first converted to either list or tuple and add it and then again convert to set
print(t2)
#print(t1)
'''
#ti[0]=5
#print(t1)
#l=[]
#l1=l+[1,2,3]
#l2=l1+[4,5,6]
#print(l2)
#l[0]=5
#print(l)
##############################set#############################
#s={1,2,3,4,2}
#print(s)
#print(s[2]) ---- Set doesn't support indexing
#s.add(51)
#print(s)
#s1=s.copy()
#print(s1)
#s1.remove(51)
#print(s1)
#s1.pop()
#print(s1)
#s1.pop(2)
#print(s1)
#l=[1,2,3,4]
#l.pop(2)
#print(l)
'''s3={4,5,6,1}
#print(s3)
#print(type(s3))
s4={1,2,3,}
#print(type(s4))
#print(s4)
#s5=s4+s3
#print(s5)
#s5=list(s4)+list(s3)
#print(s5)
#print(set(s5))
print(s3 & s4)
print(s3 | s4)
#two sets cannot be added with a + opperand but can be concatenated using & symbol
#and we can also find the common elements using | opperand
'''
'''
l1=[1,2,3,4,5]
x=set(l1)
print(x)
print(type(x))
print(list(x))
#above syntax is used to convert a list to set and again to list
'''
'''
l=[1,2,3,4]
l1=[5,6,7,8]
l.append(l1)
print(l)
print(l[4])
#Above syntax is used to print the second list which is in the first list
#The second list is treated as a single element by the first list
print(l[4][0])
#above syntax is used to print the first element in the second list
'''
'''
d={"k":10,"k1":20,30:40}
print(d.get("k"))
print(d.get(30))
print(d)
print(d.keys())
print(d.values())
print(d.items)
'''
'''
d1={}
d1["k1"]=100
print(d1)
d1["k2"]=12,24,36
print(d1)
d1[("k3","k4","k5")]=500
#in dictionary keys cannot be a list as the list is muttable which means it can
#be changed
print(d1)
#list, tuple is a ordered collection(homogenous) which means if you pass a list
#you will get the same list in the same order
#set, dictionary is a unordered collection(heterogenous) in this you will get the
#list in any order
l=[1,2,3,4]
print(sum(l))
#above syntax is used to sum the list or tuple or set or dictionary.
t=(1,2,3)
print(sum(t))
s={1,2,3}
print(sum(s))
d5={"k1":10, "k2":20,"k3":30}
print(sum(d5.values()))
#set doesnot allow duplicate values(even if we enter duplicates it will give only
#values without duplicates where as list allows duplcates and displays list along
#with duplicates
#tuple allows duplicates but values cannot be changed once assigned as it has
#only two methods i.e., index and count
'''
'''def h():
    print("hiiii")
h()

def raj():
    a=10
    b=20
    c=a+b
    print(c)
raj()

def func(a,b):
    print(a+b)
func(10,20)
'''
'''
def func1(a,b):
    c=a+b
    return c
func1(13,12)
x=func1(12,13)
print(x)
'''
#below is the example showing that if we assign a variable to the function then
#the output will be "None"
'''
def x():
    print(10)
    return 10
x()
z=x()
print(z)
'''
'''
def func4(a,b):
    c=a+b
    return c
func4(10,14)
x=func4(10,13)
print(x)
'''
#return is used to return the value but it will not be delivered as output
#when you call that function, in order to call that function you will have to
#assign that function to a variable and then execute it.
#Whereas if you have a print statement in the function and if you call that function
#it will be executed, main disadvantage of print in the function is that it
#will not return a value when called using a seperate variable, below is example
'''
def func5(a,b):
    c=a+b
    yield(c)
y=func5(1,2)
print(next(y))
#if we use Yield keyword then it next keyword should definitely be used.
'''
'''
def f():
    return 1,2

x=f()
print(x)
'''
#If we want to return both the values using return function then the above kind
#of syntax should be used.
'''
def fff():
    for x in range(10):
        yield x
fff()
z=fff()
print(next(z))
print(next(z))
'''
#for the above function if we use yield in a function you will have to assign it
#to a variable and use next in the print statement to return the first value in
#the loop or else it will return nothing. in order to return all the values in the
#loop you will have to use next for many number of times.

#Difference between class and function.
#class can have n number of fuctions and variable and you can import that class
#to make use of the functions and variables
'''
class raj:
    def func(self):
        print("Hello world")
x=raj()
x.func()

#if we are using function in a class then the function should use "self" as the
#input parameter

class raja:
    def funct(self):
        print("Hello Raj")

raja().funct()
#if we create a function in class then it is called as method.
#if we create a function normally then it is called as function.
'''
#if we use print in a function then it will be executed but if you assign that
#function to a variable and call it, it will return none and also if we use function
# in the class then the function will be execute the print statements in it.

#below is the example showing that if we assign a variable to the function then
#the output will be "None"
'''
def printassign():
    print("raj")
    print("12222")

z=printassign()
print(z)
'''
# Below is the example showing that if we assigna a variable to the class then
#the output will be the thing that is in print statement(Note that function in a
#class having print statement will be executing the output by printing the values
#that are in print statement.

'''
class a:
    def assign(self,name,sal):
        self.name=name
        self.sal=sal
        print(self.name)
        print(self.sal)
z=a()
z.assign("raj","50000")
'''
'''
class b:
    def assign(self,name="dummy",sal=20000):
        self.name=name
        self.sal=sal
    def printassign(self):
        print(self.name)
        print(self.sal)
b.assign()#this statement is not getting executed.
b.printassign()#this statement is not getting executed, it will be executed only
#if these 2 are assigned to a varaible.
#x=b()
#x.assign()
#x.printassign()
'''
'''
class a:
    def assign(self,name="dummy",sal=20000):
        self.name=name
        self.sal=sal
        print(self.name)
        print(self.sal)
a().assign()
'''
#if a variable is assigned inside the function then it is called local variable
#if a variable is assigned outside of the function then it is called gloabl variable.
#if a variable is assigned inside the class and outside the function it is called static variable.
#if a variable is assigned inside the class and inside the function then it is called instant variable
'''
a=100
def mul():
    global a
    a=10
    print("local",a)
    print("global",a)
    return a*a
mul()
x=mul()
print(x)
'''
#below is the example showing that if we assign the input numbers as global those
#can be used anywhere in any of the function.
'''
def read_number():
    global no1
    global no2
    no1=int(input("Enter no1:"))
    no2=int(input("Enter no2:"))

def add():
    read_number()
    print(no1+no2)

add()

def mul():
    read_number()
    print(no1*no2)

mul()
'''
'''
class icici:
    i_rate=10
    balance=0
    def KK(self,name,balance):
        self.name=name
        self.balance=balance
    def printvalues(self):
        print(self.name)
        print(self.balance)
        print(icici.i_rate)
        print(icici.balance)

c=icici()
c.KK("raja",20000)
c.printvalues()

sr=icici()
sr.KK("raja",2000)
sr.printvalues()


class sbi:
    i_rate=10
    balance=10000
    def deposit(self,amount):
        self.balance=self.balance+amount

    def showbalance(self):
        print(self.balance)
        print(sbi.i_rate)
#in the above example "deoposit" and "showbalance" is called identifier.
s=sbi()
s.deposit(20000)
s.showbalance()

k=sbi()
k.deposit(3000)
k.showbalance()

'''
'''
class d:
    def __init__(self):
        self.name="Raja"
        self.sal=20000
        print(self.name)
        print(self.sal)
    def display(self):
        print(self.name)
        print(self.sal)

x=d()
x.display()

'''
'''
class ee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(self.name)
        print(self.sal)

y=ee("Ram",12345)
y.display()

'''
'''
class ff:
    def __init__(self,fname="dummy", lname="dummy"):
        self.fname=fname
        self.lname=lname

    def display(self):
        print(self.fname)
        print(self.lname)


fname=input("enter First name")
lname=input("Enter Last name")
z=ff(fname=fname, lname=lname)
z.display()
'''
###########Inheritance Concepts#############
#1. single Inheritance########
'''
class a:
    def f(self):
        print("Hi")
    def f1(self):
        print("world")

class b(a):
    def f2(self):
        print("Hello")
    def f3(self):
        print("India")

z=b()
z.f()
z.f1()
z.f2()
z.f3()
print(b.__mro__)

x=a()
x.f()
x.f1()
x.f2() #will get an error as class a cannot call the methods in class b
x.f3() #will get an error as class a cannot call the methods in class b
'''

#1.a. Single Inheritance with constructor
'''
class a:
    def __init__(self,fname,sal):
        self.fname=fname
        self.sal=sal
        print("hi")

    def f1(self):
        print(self.fname)
        print(self.sal)
        print("Hello World")

class b(a):
    def __init__(self,fname,sal):
        self.fname=fname
        self.sal=sal
        print("hey")

    def f2(self):
        print(self.fname)
        print(self.sal)
        print("wt r u doing")

#z=a("raj",123)
#z.f2() #will get an error as class a cannot call the method in class b

x=b("ram",12345)
x.f2()
x.f1()
'''
#why did class a first method didn't display hi?
#how do i know if the answer that is displayed is because of the constructor
#working, i dont think constructor is working in class a if i call class b.

#########2. Multilevel Inheritance#####################
'''
class bank:
    def deposit(self,name,amount):
        self.name=name
        self.amount=amount
    def display(self):
        print(self.name)
        print(self.amount)

class sbi(bank):
    def a(self,fname,lname,balance):
        self.fname=fname
        self.lname=lname
        self.balance=balance
    def display1(self):
        print(self.fname)
        print(self.lname)
        print(self.balance)

class icici(sbi):
    def a1(self,bal):
        self.bal=bal
    def display2(self):
        print(self.bal)
'''
'''
z=bank()
z.deposit("raj",1000)
z.display()
'''
'''
s=sbi()
s.a("ram","lal",10000)
s.display1()
s.deposit("Raghu",1000)
s.display()
'''
'''
i=icici()
i.a("Sam","Robert",10000)
i.display1()
i.deposit("Rama",9890)
i.display()
i.a1(3989)
i.display2()
'''
#########3. Multiple Inheritance##################
'''
class a:
    def f(self):
        print("Hi")

class b:
    def f1(self):
        print("Hello")

class c:
    def f2(self):
        print("How are you")

class d(a,b,c):
    def f3(self):
        print("I am good")

z=d()
z.f()
z.f1()
z.f2()
z.f3()
'''
############ Multiple Inheritance with constructor#################
'''
class a:
    def __init__(self):
        print("hi")

class b:
    def __init__(self):
        print("Hello")

class c:
    def __init__(self):
        print("how are you")

class d(a,b,c):
        def f(self):
            print("I am good")

z=d()
z.f()

#a=c()
'''

# why did only first method work and rest all didn't work?

###############Polymorphism##############
'''
class raj:
    def __init__(self,num):
        self.num=num
    def add(self):
        print(self.num+self.num)

class yadav(raj):
    def __init__(self,num):
        self.num=num
    def mul(self):
        print(self.num*self.num)

#b=raj(5)
#b.add()

a=yadav(4)
a.mul()
a.add()
'''

###########Function Overloading#############
#In python there is no function overloading
#there is only operator overloading
#Below is the example for operator overloading
'''
print(20+30)
print("Raj"+"Yadav")

l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)

######Multiply Operator######

l1=[1,2,3]
print(l1*3)

print(10*20)
print("Raj"*3)
'''
#Below is the example for methond overloading
'''
class aa:
    def f(self):
        print("hi")
    def f(self,num):
        print(num)
    def f(self,num,num1):
        print(num,num1)

c=aa()
c.f(1,2)
c.f()
'''
#For the above kind of scenario we will use star argument, below is the example
'''
class bb:
    def f(self,*args):
        print(sum(args))

b=bb()
b.f(1,2,3)
'''

##############Method Overriding#################
'''
class raj:
    def __init__(self,no3,no4):
        self.no3=no3
        self.no4=no4
    def bb(self):
        print(self.no3+self.no4)
        print(self.no3*self.no4)

class yadav(raj):
    def __init__(self,no3,no4):
        self.no3=no3
        self.no4=no4
    def bb(self):
        print(self.no3/self.no4)
        print(self.no3-self.no4)

#a=raj(1,2)
#a.aa()

b=yadav(1,2)
b.bb()
'''
#In the above example if you see in both the classes methods names are same
#but when we call that method you can see that the method in only class yadav
#is executed but not the method in class raj. In order to execute both the
#methods in both the classes we use the super() keyword.
#Note: we can use super keyword only when both the methods have same name
#below is the example using the super keyword.
'''
class raj():
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def aa(self):
        print(self.no1+self.no2)
        print(self.no1-self.no2)

class yadav(raj):
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def aa(self):
        print(self.no1*self.no2)
        print(self.no1/self.no2)
        super().aa()

a=yadav(1,2)
a.aa()
'''
### Another example to demonstrate method overriding is possible####
'''
class hari:
    def aa(self,no1,no2):
        print(no1+no2)

class babu(hari):
    def aa(self,no1,no2):
        print(no1*no2)
        super().aa(no1,no2)

a=babu()
a.aa(4,5)
'''
# Inorder to install any module in python below is the command that should be used.
#pip install selenium
#pip install mysql
#pip install numpy

#In order to check if any module is installed in your system, below is the code.
#python -c "import numpy"

#### What is the difference between package and module ##############
#Package is nothing but collection of sub packages and modules
#let us consider there are 2 folder in a drive, so first folder is called package
#second folder is called sub package
#and the files that are in the 2nd folder are called modules.

#To install any module in python below is the command that should be typed in cmd prompt

#pip install selenium

#To check if that module is in python below is the command that should be used in cmd prompt:

#python -c "import numpy"
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
'''

# In the above example you will get an error Message stating 'chromedriver' executable needs to be in PATH.
#so for this we will have to put the chrome browser in the path c:users:U6029297

#ask hari on how to put chrome driver in that path and how to identify the path
#ask hari on the two types of syntax to import selenium(import from selenium is giving error)


import selenium.webdriver
driver = selenium.webdriver.Chrome()
aa.get("https:/www.facebook.com")








































