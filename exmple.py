S="java programming"
S="python"+S[4:]
print(S)

#ctr+/ (for commnetin no of lines with #)

l=[1,2,3,4,5,6,7,8,9]
#print(l[0:4])
print(l[-1])
l.reverse()
print(l)
print(l[::-1])


l1=[1,2,3,4,5,6,8]
for x in range(1,9):
    if x in l1:
        pass
    else:
        print(x)





class b:


    def f(self):
        print("hi")

    def f1(self):
        print("hello")


b1=b()
b1.f()
b1.f1()


class d:
    def __init__(self,name):
        self.name=name
        print("hiiiiiiiiiiiii")
    def f3(self):
        print(self.name)
        print("hw r u")

d1=d("hari")
d1.f3()


