# class a:
#     def f(self):
#         print("hii")
#
#     def f1(self):
#         print("hello world")
#
#
# class b(a):
#     def f(self):
#         print("hey")
#     def f3(self):
#         print("wt r u dg")
#
#
# a1=a()
# a1.f()
# a1.f1()
# #a1.f2() error


# b1=b()
#
# b1.f3()
# b1.f()
# b1.f1()
#
# print(b.__mro__)


# class a:
#     def __init__(self,fname,sal):
#         self.fname=fname
#         self.sal=sal
#         print("hii")
#
#     def f1(self):
#         print(self.fname)
#         print(self.sal)
#         print("hello world")
#
#
# class b(a):
#     def __init__(self,fname,sal):
#         self.fname=fname
#         self.sal=sal
#         print("hey")
#     def f3(self):
#         print(self.fname)
#         print(self.sal)
#         print("wt r u dg")
#
#
# #a1=a("dd",5000)
#
# #a1.f1()
# #a1.f2() error
#
#
# b1=b("gg",1000)
#
# b1.f3()
# b1.f1()


# class bank:
#     def deposit(self,name,amount):
#         self.name=name
#         self.amount=amount
#     def display(self):
#         print(self.name)
#         print(self.amount)
#
#
# class sbi(bank):
#     def a(self,fname,lname,balance):
#         self.fname=fname
#         self.lname=lname
#         self.balance=balance
#     def displa(self):
#         print(self.fname)
#         print(self.lname)
#         print(self.balance)
#
# class icici(sbi):
#     def a1(self,bal):
#         self.bal=bal
#
#     def dis1(self):
#         print(self.bal)



# b=bank()
# b.deposit("ff",10000)
# b.display()

# s=sbi()
# s.a("kri","sh",1000)
# s.displa()
# s.deposit("dd",2000)
# s.display()
#
# i=icici()
# i.a1(20000)
# i.dis1()
# #
# i.a("ram","krishna",5123)
# i.displa()
#
# i.deposit("dddd",10000)
# i.display()
#
#
#
#
# class a:
#     def afun(self,name,sal):
#         print("i am a afun of class a")
#         self.name=name
#         self.sal=sal
#         print(self.name)
#         print(self.sal)
#
#
# class b(a):
#     def bfun(self,fname,amount):
#         print(" i am a bfun of b class")
#         self.fname=fname
#         self.amount=amount
#         print(self.fname)
#         print(self.amount)
#
# class c(b):
#     def cfun(self,lname,balance):
#         print("i am a cfun of class c")
#         self.lname=lname
#         self.balance=balance
#         print(self.lname)
#         print(self.balance)
#
#
#
# c1=c()
# c1.afun("krishna",1000)
# c1.bfun("kk",2000)
# c1.cfun("aa",3000)

'''
class a:
    def f(self):
        print("hi")

class b:
    def f1(self):
        print("heelo")

class c:
    def f2(self):
        print("world")

class d(a,b,c):
    def f3(self):
        print("hi all functions claaed")


d1=d()
d1.f3()
d1.f()
d1.f1()
d1.f2()
'''
#################Interview Questions#################
#Example to replace a number in a list with another number
'''
l=[1,2,3,4,5]
l.append(6)
print(l)
print(l.index(1))
l[1]=7
print(l)
'''
#How to check if the string is empty
'''
s=""
if len(s)==0:
    print("String is empty")
else:
    print(len(s))
'''
#####################File Handling####################
'''
f=open("Rajracer.txt","w")
f.write("Hello")
f.close()
'''
#Syntax to read the number of letters in the file#
#if you dont mention anything after file name in the below syntax then it automatically
#considers it as read mode.
#to read the total content in the file we use read() syntax
'''
f=open("Rajracer.txt","r")
x=f.read()
print(x)
'''
#to read the first line in the file we use readline() syntax
'''
f=open("Rajracer.txt","r")
x=f.readline()
print(x)
'''
#to read the second line in the file we have to use readline() syntax twice.
'''
f=open("Rajracer.txt","r")
x=f.readline()
x=f.readline()
print(x)
'''
#to read the same line twice using readline() we will have to use another
#syntax called f.seek(0) and then use f.readline() syntax to call same line.
'''
f=open("Rajracer.txt","r")
x=f.readline()
f.seek(0)
x=f.readline()
print(x)
'''
#to call all the lines in the file in the list format we use readlines()
'''
f=open("Rajracer.txt","r")
y=f.readlines()
print(y)
'''
#to read the particular line in the file then we will have to give the index position
#same as how we give in the list.below is the example
'''
f=open("Rajracer.txt","r")
z=f.readlines()
print(z[4:6])
f.close()
'''

#here if we use write function it will replace all the data in the file with
#what we have written, where as append function will add the text that we have
#written to the existing data
'''
f=open("Rajracer.txt","w")
f.write("Hi How are you")
f.close()

f=open("Rajracer.txt","r")
x=f.read()
print(x)
'''
#Syntax to append the data in the file
'''
f=open("Rajracer.txt","a")
z=f.write("I am good")
print(z)
f.close()
'''
#Below is the syntax showing what is the type of the read(), readline(),readlines()
'''
f=open("Rajracer.txt","r")
print(type(f.read()))
print(type(f.readline()))
print(type(f.readlines()))
'''

#below is the syntax showing the count of number of characters in the input
#that we are passing
'''
f=open("Raj.txt","w")
z=f.write("how are you")
print(z)
'''
#below is the method showing that we dont have to close the file by using the
#syntax f.close() everytime we open the file using f=open("Rajracer.txt")
'''
with open("Rajracer.txt") as f:
    x=f.read()
    print(x)
'''
#####################Try Catch############
'''
try:
    f=open("Rajas.txt","r")
    f.read()
except Exception as e:
    print(e)
finally:
    print("Program End")
'''
#Append and write will create a new file if it doesn't find the file name.
#In Try and except if we use finally both the try or except along with finally
#will be executed.

#Below is the syntax to create a new word document and save.
'''
from docx import document

document = Document()
document.save("test.docx")
'''
#Topics in Regular expressions will be in below link
#   https://docs.python.org/2/library/re.html
#Below is the syntax to split the string based on the alphabet in that string
'''
import re
s="Rajashekar"
#x=re.split("s",s)
x=re.split("R",s)
print(x)
'''
#Below syntax is using the regular expression where as the one below that is
#using a method called replace.
'''
import re
h="Java Programming"
z=re.sub("Java","Python",h)
print(z)
'''
#below syntax is using a replace function.
'''
h="Java Programming"
z=h.replace("Java","Python")
print(z)
'''
#Below syntax is for "Match" function.
'''
import re
k="Java Programming"
s=re.match("Java",k)
print(s)
'''
#Below is the syntax for "Search" function
'''
import re
k="Java Programming"
z=re.search("Program",k)
print(z)
'''
#Difference Between Match and Search, Match function will only work if the word
#that you are searching for is in the first place of that string, else it would
#return None as the output, where as if you use Search function then it would
#return the position of that word if it is anywhere in that string.
#Both "Match" and "Search" functions will return the required value even if it
#matches with the given string has the partial match.


#Below is the function for "Findall" syntax
#It finds and returns the given keyword in the string, if it is found 3 times then
#it will return it 3 times and the output will be in the list format.
'''
import re
q="Java Programming is the heart of Java, Java is hard"
z=re.findall("Java",q)
print(z)
'''
import re
r="krishnaveni"
#below syntax is to print each(single) alphabets in the string seperately
#c=re.findall("\w",r)
#below syntax is to print two alphabets in the string seperately
#c=re.findall("\w\w",r)
#below syntax is to print three alphabets in the string seperately
#c=re.findall("\w\w\w",r)
#with the below syntax we can also mention the number of character you want the
#string to be split into.
#c=re.findall("\w{3}",r)
#Below syntax will give you the last alphabet in the given string
#c=re.findall("\w$",r)
#Below syntax will give you the first alphabet in the given string
#c=re.findall("^\w",r)
#Below syntax will give you the whole string
#c=re.findall("\w+",r)
#print(c)
#Note: When printing the output if say the string has 10 alphabets and if you ask
#it to be split into 3 alphabets each then the last alphabet is left alone and
#will not be printed.

#Below is the syntax to print each alphabet in a string seperately
'''
import re
c="krishnaveni"
for x in c:
    z1="".join(str(x))
    print(z1)
    print(type(z1))
'''

#Below syntax is used to find the numbers in the string and then convert them
#to numbers and then sum those numbers
#In the below syntax findall("\d") is used to find only the numbers i.e., digits.
'''
s="123456rajafj89876542"
z1=re.findall("\d{2}",s)
print(z1)
l=[]
for x in z1:
    y1=int(x)
    z1=l.append(y1)

print(l)
print(sum(l))
'''

#Below syntax is used to find the small alphabets in the given string
'''
q="afjdjojafpdaPAVAd1354536546dadagadgsa"

import re
#s1=re.findall("[a-z]",q)
s1=re.findall("[A-Z]",q)
print(s1)
'''

#Below syntax is used to find if the ip address is valid or not
'''
def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if  0<=int(item) <=255:
            return False
    return True

validIP(1.1.1.1)
'''

#List Comprehension

'''
counter,
map,
reduce - Amuls academy
'''
'''
for x in range(10):
    print(x*x)

x=[x**2 for x in range(10) if x%2==0]
print(x)

z={x**2 for x in range(10)}
print(z)
'''
'''
s="rajashekarfromhyd"
z1={i:s.count(i) for i in s}
print(z1)
'''
#Collections Module
'''
import collections
print(collections.Counter(s))

d={}
for x1 in s:
    if x1 not in d.keys():
        d[x1]=1
    else:
            d[x1]=d[x1]+1

print(d)
'''
'''
import collections
l1=[1,2,3,4,1,2,3,4,5,6,7,5,6,7]
print(collections.Counter(l1))
'''
'''
s2="hari babu krishna shekar ram ram from user hari"
s3=s2.split()
print(s3)

d3={}
for x3 in s3:
    if x3 not in d3.keys():
        d3[x3]=1
    else:
        d3[x3]=d3[x3]+1

print(d3)
'''
#Lambda Function
#Lambda Functions are the functions that are defined without any name, so they are
#also called as anonymus functions.
#Lambda functiona are defined using the keyword "lambda".
#Below is syntax for lambda function
#lambda arguments:expression
#Lambda function can contain more than one arguments but it should have only one
#expression
#Lambda function is used in another functins such as "Map", "reduce" and "filter"
#usually a function is defined using the keyword def and function name
#below is the example
#def fun():
'''
l4=["hari@gamil.com","babu@yahoo.com","shekar@hotmail.com","siva@gogle.com"]
l4.sort()
print(l4)
l4.sort(key=lambda x:x.split("@")[1])
print(l4)
'''
#Lambda Expressions

#Map Function - it is a built-in function, and this function it is used to apply
#a function to all the elements of a sequence
#Map Syntax - map(function, seq)
#sequence can be a list, tuple or strings
#below is the example using the map function:
a=[1,2,3,4]
'''
def square(x):
    #print(x*x)
    return x*x

#map(square,a)
#If we are using python 2.version then there is no need to mention list just mention
#above syntax
z1=list(map(square,a))
print(z1)

z2=tuple(map(square,a))
print(z2)
'''
#if we use print in the function then that individual square output is printed,
#but if we use return then the output is printed in the form of list.

#Below is the example of map function using lambda function.
'''
z3=list(map(lambda x:x*x,a))
print(z3)

z4=tuple(map(lambda x:x*x,a))
print(z4)
'''
#Here in the above expression "lambda x:x*x" is the function and a is the sequence.
#In the same way for Lambda "x" is the argument and "x*x" is the expression
'''
b=[5,6,7,8]
c=[9,1,2,3]
z5=list(map(lambda x,y,z:x*y*z,a,b,c))
print(z5)
'''
#Filter Function
#Filter function will filter the element of the iterator based on some function.
#This is used to filter the unwanted elements.
#Filter Syntax
#filter(function,iterables)
#Filter function will return the element from iterable when the function is TRUE.
#below is the example to print even numbers without using filter
'''
for x in range(1,11):
    if x%2==0:
        print(x)
#Below is using a filter
z=list(filter(lambda x:x%2==0,range(1,11)))
print(z)
'''
#In the map function we were using more than one seq but in filter function we
#can use only one itterable
#Here we can print even numbers by both filter and for loop, but as filter is
#In-built function it is faster.

#Reduce Function
#Reduce function will reduce the itterable to single element using sum or product functions.
#if we want to perform the computation on the list or tuple we can use reduce function.
#Reduce function syntax:
#reduce(function, itterables)
#Itterable is nothing but anything that can be looped over like, list, tuple, string or rain functions.
#in order to use reduce function we need to import the module functools
'''
import functools
a=[1,2,3,4,5]
print(functools.reduce(lambda x,y:x+y,a))
'''
#############################################################

#Default Dictionary
'''
from collections import defaultdict
d4=defaultdict(lambda:0)
print(d4['one'])
print(d4['two'])
'''
#Default dictionary by default will give only the assigned value even if anything
#else is passed.
#In the above example by default "0" is passed but if we try to pass any other
#value it will still give the output as 0.

#Ordered Dictionary
'''
import collections
d=collections.OrderedDict()

d["a"]=1
d["b"]=2
d["c"]=3
print(d)
'''
#As we know that dictionary is an un ordered list.
#But the ordered dictionary will help us make it as ordered.
#Below is the example
'''
d1={}
d1["a"]=1
d1["b"]=2
d1["a1"]=1
d1["b1"]=2
d1["a2"]=1
d1["b2"]=2
d1["k"]=1
d1["j"]=2
print(d1)
'''
#Any and All functions
'''
L=[True,True,False]
print(any(L))
print(all(L))
'''
#Any will give output as True if any one of the boolean expression is true.
#All will give output as True only if all the boolean expressions are true.
#In the above example for All the output is False as all the expressions are not True.
#In the same way for Any the output is True as one of the expression is True.

#Name Mangling
#Name Mangling is used to protect the data from accessing it directly, in order to
#Access that data it should be called using the class name.
'''
class raj:
    balance=1000
    _amount=2000 #Private variable
    __total=balance+_amount #Protected Variable

h=raj()
print(h.balance)
print(h._amount)
#print(h.__total)
#The above print statement throws error as it is protected, it can only be accesed
#using the class name.
print(h._raj__total)
'''
#Another example
'''
class shekar:
    __s=3000
    def __init__(self,name,sal,amount):
        self.name=name
        self._sal=sal
        self.__amount=amount
    def display(self):
        print(self.name)
        print(self._sal)
        print(self.__amount)

k=shekar("raj",1000,2000)
#print(k.display())
#k.display()
print(k._shekar__s)
'''

#Another Example for Name Mangling
'''
class stack:
    def __init__(self):
        self.__storage = []
    def push(self,value):
        self.__storage.append(value)

s=stack()
s.push("Krishna")
s.push("Dimpe")
print(s._stack__storage)
'''
#Same Example without Name Mangling
'''
class stack:
    def __init__(self):
        self.storage=[]
    def push(self,value):
        self.storage.append(value)

s=stack()
s.push("Raj")
print(s.storage)
'''

#Frozen Set
#Frozen set is nothing but freezing the set or list or tuple so that the set cannot
#be appended
'''
a=[1,2,3,4]
a.append(5)
print(a)
'''
#Above example shows how to append a value to the list.
'''
g={1,2,3,4,5}
g.add(6)
print(g)
'''
#Above example shows how to add a value to a tuple.
'''
k={1,2,3,4}
f=frozenset(k)
print(f)
#f.add(5) #This will throw an error
'''
#In the above example once the tuple is frozen we will not be able to add values.
#Also note that frozen set will be able to freeze on the items that are itterable.
#such as string, list, tuple etc...
#Below is the example showing that.
'''
f=frozenset("10")
print(f)
f=frozenset(10)
print(f)
'''

#Multithreading

import threading

def mul(num):
    print(num*2)
    #print(" ")

def square(num):
    print(num**2)

if __name__=="__main__":
    t1=threading.Thread(target=square,args=(10,)) #This syntax Creates Thread1
    t2=threading.Thread(target=mul,args=(10,)) #This syntax Creates Thread2

    t1.start() #Starts Thread1
    t2.start() #Starts Thread2

    t1.join() #Stops Thread 2 from executing until Thread 1 is executed.
    t2.join()

    print("Done")






