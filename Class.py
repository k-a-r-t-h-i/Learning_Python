class Trail:    # class with default constructor
    h=10    #class variable
    def m1(self):
        print("hello")

t1=Trail()
print(t1.m1) #this prints method info
t1.m1()     #this calls the method m1
print(t1.h) #accessing with instance
print(Trail.h) #accessing with class name 

print("-----------------------------------------------")

class Trail2:   # class with a constructor
    def __init__(self,a):  # a is an instance variable
        self.a=a
    def prt(self):
        print(self.a)

t2=Trail2(23)
print(t2.a)
t2.prt()

'''
Output:

<bound method Trail.m1 of <__main__.Trail object at 0x00EEE>>
hello
10
10
-----------------------------------------------
23
23
'''