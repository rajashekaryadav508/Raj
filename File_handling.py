'''
import sys
print(sys.argv[0])
print(sys.argv)


import selenium.webdriver

driver=selenium.webdriver.Chrome()
driver.get("https://www.fb.com")




f=open("hari123.txt","w")
f.write("hello")
f.close()

#f=open("hari123.txt")
#x=f.read()
#print(x)
#print(f.read())



#y=f.read(5)
#print(y)
#print(f.readline())

#print(f.readline())
#print(f.readlines())
#print(type(f.read()))
#x=f.readlines()
#print(x[4:8])
#f=open("hari123.txt","a")
#z=f.write("hfldfdsfshfjsdf")
#print(z)

#f=open("hari123.txt","w")
#f.write("gdkdgahsdgaskdasd")
#f.close()


with open("hari123.txt") as f:
    f.read()
    
    #f.close()

from docx import Document

document = Document()
document.save('test.docx')
'''

import sqlite3

f.close()
