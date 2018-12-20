'''x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=x+y
print("The sum of x and y is",x+y)
'''
'''-------------------------------------------------'''
'''k=int(input("enter the value of k:"))
if(k==10):
    print("The Entered value is correct")
else:
    print("The Entered value is incorrect")
    '''
'''-------------------------------------------------'''
'''
k1=int(input("Enter the value of k1:"))
k2=int(input("Enter the value of k2:"))
if(k1==k2):
    print("Both the values are same")
elif(k1>k2):
    print("K1 is greater than k2")
else:
    print("k2 is greater than k1")
'''
'''-------------------------------------------------'''
'''
a=10
b=20
min=a if a>b else b
print(min)
'''
'''-------------------------------------------------'''
'''a,b=10,20
c=a+b
print("Sum of a and b is",c)
'''
'''-----------------------------------------------'''
'''Telugu=int(input("Enter Telugu Marks:"))
Hindi=int(input("Enter Hindi Marks:"))
English=int(input("Enter English Marks:"))
Maths=int(input("Enter Maths Marks:"))
Science=int(input("Enter Science Marks:"))
Social=int(input("Enter Social Marks:"))
if((Telugu<35 or Hindi<35 or English<35 or Maths<35 or Science<35 or Social<35)):
    print("Failed in All Subjects")
else:
    print("Passed in all the subjects")'''
'''--------------------------------------------------------'''
'''TotalMarks=int(input("Enter total number of Marks:"))
if(TotalMarks>600):
    print("Enter Marks between 0 and 600")
elif(TotalMarks>=450 and TotalMarks<=600):
    print("Passed in First class with Distinction")
elif(TotalMarks<450 and TotalMarks>=360):
    print("Passed in First class")
elif(TotalMarks<360 and TotalMarks>=300):
    print("Passed in Second class")
elif(TotalMarks<300 and TotalMarks>=210):
    print("Passed in Third class")
else:
    print("Failed")
'''
'''-------------------------------------------------------'''
'''
PIN_Number=1508
Balance=50000
PIN_Number=int(input("Enter the PIN:"))
if(PIN_Number==1508):
    print("Entered PIN is correct")
    Withdraw=int(input("Enter the amount for withdrawl:"))
    if(Withdraw<Balance and Withdraw%100==0 and Withdraw!=0):
        print("Entered amount is correct")
        Balance=Balance-Withdraw
        print(Balance)
    else:
        print("Enter the amount less than balance and Enter amount in multiples of 100's")
else:
    print("Entered PIN is incorrect")
'''
'''---------------------------------------------------------'''
'''CLASS 2 (10/10/2018)'''
'''for x in range(10):
    print(x)
print("-----------")
for x in range(1,10):
    print(x)
print("------------")
for x in range(1,10,2):
    print(x)
for x in range(0,10,2):
    print(x)
for x in range(10,1,-1):
    print(x)
print("--------------")
for x in range(10,1,-2):
    print(x)
'''
'''to find the even numbers'''
'''for x in range(1,10):
    if(x%2==0):
        print(x)
'''
''' to find the odd numbers'''
'''
for x in range(1,10):
    if x%2==1:
        print(x)
'''
'''while loop'''
'''
i=1
while(i<10):
    print(i)
    i=i+1
'''
'''for printing the tables'''
''' this methond will not end the statement but will come again asking for input'''
'''
i=1
while(True):
    tno=int(input("Enter tno"))
    eno=int(input("Enter eno"))
    for i in range(1,eno+1):
        print(tno,"*",i,tno*i)
        i=i+1
'''
''' but this will not ask for input again and will stop'''
'''
i=1
tno=int(input("Enter the starting number"))
eno=int(input("Enter the ending number"))
while(i<=eno):
    for i in range(1,eno+1):
        print(tno,"*",i,"=",i*tno)
        i=i+1
'''
'''using break statement'''
'''
for x in range(1,10):
    if(x==2):
        break
    else:
        print(x)
'''
'''
i=1
while(i<10):
    if(i==5):
        break
    else:
        print(i)
        i=i+1
else:
    print("Somevalue")
'''
Print(help(id))- this is syntax(Type help() for interactive help, or help(object) for help about object.
'''
''for printing the numbers in sequence'''
'''
for x in range(3):
    for y in range(1,4):
        print(y,end=" ")
    print(" ")
'''
'''for printing the numbers in reverse order below is the syntax
for x in range(10,1,-1):
    print(x)
'''
'''
s="raj"
print(s)
s[4]=1
print(s)
'''
'''to iterate the string by calling one letter in the string at a time below is used'''
'''
s="raj"
for a in s:
    print(a)
'''
'''
z=123
z[3]=4
print(z)
'''
'''if you want to print a number in an order then below is the code'''
'''
z=123
a=str(z)
for i in a:
    print(i)
'''
#l=[1,2,3,4]
#print(l)
#print(l[2])
#print(l[:])
#print(l[:1])
#print(l[:2])
#print(l[2:])
#print(l[0:3:])
#print(l[0:3:-1])
#print(l[:3:0-1])
#print(l[:3-1])
#print(l[::-1])
#z=[1,2,3,4]
#l=[5,6,7,8]
#s="rajashekar"
#l.append(z)
#print(l)
#z.append(l)
#print(z)
#l.extend(z)
#print(l)
#l.append(s)
#print(l)
#l.extend(s)
#print(l)
#l.extend(4)
#print(l)
#l.append(4)
#print(l)
''' to print the exact number that you want from the list'''
'''
l1=[3,5,2,1,6,6,7,8,9]
for x in l1:
    if(x==6):
        print(x)
'''
#l2=[3,5,2,1,6,6,7,8,9]
#l2.sort() will sort the list in ascending order
#print(l2)
#l2.reverse() will reverse the list
#print(l2)
#l2.remove(8) will remove the specified number from the list
#print(l2)
#l2.pop() will pop out the last number in the list
#print(l2)
#print(l2.index(9)) used to find the index value of that particular number
#print(l2.count(6)) used to count the no of times that number is repeated
#l3=l2.copy()
#print(l3)
#l3.clear()
#print(l3)

#l4=[3,4,0,5,7,6,1,2,9]
#for i in range(1,11):
#    if i not in  l4:
#        print(i)

'''
'''
'''
n=1234
a=str(n)
n=int(a[::-1])
print(n)
print(type(n))
'''
'''
l4=["hari","babu","raj","kumar","srinu"]
l5=["kk","jj","kumar","krishna","ll","mm"]
for x in l4:
    if x in l5:
        print(x)
'''
'''s="wonders"
#print(s[::-1])
#print(s[2])
s="".join(sorted(s))
print(s)
'''
#11/10/2018

#t=()
#t1=t+(1,2,3,4,1)
#print(t1)

#t=(1,2,3,4,1)
#print(t.index(2))
#print(t.count(1))
#print(t[:2])
t="raj",1,2
#print(type(t))
#print(t[:2])
#t1=()
#t1[0]=5 error
#print(t1)

s={1,2,3,4,5}
print(s)
s.add(51)
print(s)



















