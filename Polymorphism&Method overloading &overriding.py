
#######################Polymorphism####################
'''
class hari:
    def __init__(self,num):
        self.num=num
    def add(self):
        print(self.num+self.num)

class babu(hari):
    def __init__(self,num):
        self.num=num
    def mul(self):
        print(self.num*self.num)


#h=hari(5)
#h.add()


b=babu(3)
b.mul()
b.add()
'''
###########Method overloading#############
#Here in the below example only the last method will be executed and other methods will not be executed as it will not allow to enter the less arguments, for this we will go for star arguments which will help us in calling any
#of the method, actually there is no need for writing number of methods. you can simply give star argument as the input parameter and you can give as many input parameters as you want.
'''
class kk:
    def f(self):
        print("hii")
    def f(self,num):
        print(num)
    def f(self,num,num1):
        print(num,num1)

c1=kk()
c1.f(2,3)

'''
#Below is the example for method overloading, it is possible using the star argument
'''
class we:
    def f(self,*args):
        print(sum(args))

w=we()
w.f(123,123)
'''

#operator overloading is possible but method overloading is not possible in python

#Above is the example showing that method overloading is not possible(Method overloading is nothing but execution of all the methods in all the classes)
'''
print(2+3)
print("hari"+"1")
'''
######## Method overriding#############
'''
'''
#below are two examples for operator overriding
'''
class mm:
    def f4(self,no1,no2):
        print(no1+no2)


class vv(mm):
    def f4(self,no1,no2):
        print(no1*no2)
        super().f4(no1,no2)


v=vv()
v.f4(3,4)

'''
'''


'''
'''
class bank:
    def __init__(self,no3,no4):
        self.no3=no3
        self.no4=no4
    def f6(self):
        print(self.no3+self.no4)
        #print(self.name)
        #print(self.bal)


class sbi(bank):
    def __init__(self,no3,no4):
        self.no3=no3
        self.no4=no4
        
    def f6(self):
        super().f6()
        print(self.no3*self.no4)
        #print(self.name)
        #print(self.bal)


s=sbi(12,123)
s.f6()

#b=bank(123,1234)
#b.f6()
'''        


#To install any module in python below is the command that should be typed in cmd prompt

#pip install selenium

#To check if that module is in python below is the command that should be used in cmd prompt:

#python -c "import numpy"

#### What is the difference between package and module ##############
#Package is nothing but collection of sub packages and modules
#let us consider there are 2 folder in a drive, so first folder is called package
#second folder is called sub package
#and the files that are in the 2nd folder are called modules.

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

# In the above example you will get an error Message stating 'chromedriver' executable needs to be in PATH.
#so for this we will have to put the chrome browser in the path c:users:U6029297

#ask hari on how to put chrome driver in that path and how to identify the path
#ask hari on the two types of syntax to import selenium(import from selenium is giving error)


