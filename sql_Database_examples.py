'''import sqlite3 as sql
conn=sql.connect("hari_db")
curs=conn.cursor()
curs.execute("create table emp(id number primarykry,name text,cno number)")
conn.commit()
conn.close()

import sqlite3 as sql
conn=sql.connect("hari_db")
curs=conn.cursor()
try:
    curs.execute("create table emp(id number Primarykey,name text,cno number)")
except sql.OperationalError:
    print("table is already available")

    
conn.commit()
conn.close()
'''
'''import sqlite3 as sql
conn=sql.connect("hari_db")
curs=conn.cursor()
try:
    curs.execute("insert into emp values(101,'hari',98756898996)")
except sql.OperationalError:
    print("change id no")
finally:
    conn.commit()
    conn.close()

import sqlite3 as sql
conn=sql.connect("hari_db")
curs=conn.cursor()
try:
    curs.execute("insert into emp values(101,'hari',98756898996)")
except sql.OperationalError:
    print("change id no")
finally:
    conn.commit()
    conn.close()
'''

'''import sqlite3 as sql
def readinput():
    idno=int(input("idno"))
    name=input("name")
    cno=int(input("cno"))
    return idno,name,cno
def insertintodb():
    conn=sql.connect("hari_db")
    curs=conn.cursor()
    result=readinput()
    try:
        curs.execute("insert into emp values(?,?,?)",result)
    except :
        print("change id no")
    finally:
        conn.commit()
        conn.close()



insertintodb()


import sqlite3 as sql
conn=sql.connect("hari_db")
curs=conn.cursor()
val=[
    (103,"krishna",987456123),
    (110,"ram",789456123)
    ]
try:
    curs.executemany("insert into emp values(?,?,?)",val)
except:
    print("change id no")
finally:
    conn.commit()
    conn.close()

import sqlite3 as sql
conn=sql.connect("hari_db")
curs=conn.cursor()
curs.execute("select *from emp")
list=curs.fetchmany(2)
for x in list:
    print(x)
conn.commit()
conn.close()


import mysql.connector
conx=mysql.connector.connect(user='scott',password='password',host='127.0.0.1',database='employee')
curs=conx.cursor()
cursor.execute("ctreate table emp2(id number Primarykey,name text,cno number)")
conn.commit()
conn.close()
'''
'''try:
    f=open("sample.txt")
    print(f)
except:
    print("print file not found")

print("thanks")

try:
    f=open("sample.txt")
    s=f.read()
    print(s)
    f.close()
except:
    print("file not found")

try:
    f=open("sample.txt")
    s=f.readline()
    print(s)
    s1=f.readline()
    print(s1)
    f.close()
except:
    print("file not found")


try:
    f=open("sample.txt")
    s=f.readlines()
    print(s)
    f.close()
except:
    print("file not found")

try:
    f=open("sample.txt")
    s=f.read(6)
    print(s)
    f.close()
except:
    print("file not found")

'''
'''try:
    f=open("sample.txt","w")
    f.write("hello krishna")
    print("wring file")
    f.close()
except:
    print("file not found")

try:
    f=open("sample.txt","a")
    f.write("hello ram")
    print("wring file")
    f.close()
except:
    print("file not found")

'''
import docx
d=docx.document()
d.add_heading("python text file")
d.add_paragraph("dont sleepin the class")
d.save(dummy2.docx)

















    











































































