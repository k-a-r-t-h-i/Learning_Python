#Inheritace concepts
#properties of parent can be accessed by child but not vice versa
#properties of a class are data members and member functions

#simple example
class Parent:
    def parent_asset(self):
        print("I'm Parent! I'm having 600 Lakhs")

class Child(Parent):
    def child_asset(self):
        print("I'm Child! I'm having 100 Lakhs")

print("simple example")
obj=Child()
obj.child_asset()
obj.parent_asset()
print("--------------------------------------")

#Types of inheritance

#base class
class Person(): #all classes are subclasses of object class even if not mentioned
    def __init__(self,age,name):
        self.age=age
        self.name=name
    
    def getname(self):
        print("name:", self.name)

    def getage(self):
        print("age:", self.age)
print("base class")
p1=Person(19,"Karthi")    
p1.getname()
p1.getage()
print("--------------------------------------")


#single level inheritance
class Employee(Person): 
    def __init__(self,age,name,designation):
        super().__init__(age,name)
        self.designation=designation
    def getdesignation(self):
        print("designation:",self.designation)
print("single level inheritance")
e1=Employee(23,"Lokesh","Manager")
e1.getname()
e1.getage()
e1.getdesignation()
print("--------------------------------------")


#Multilevel inheritance
class Citizen(Employee): 
    def __init__(self,age,name,designation,aadhar):
        super().__init__(age,name,designation)
        self.aadhar=aadhar
    def getaadhar(self):
        print("aadhar:",self.aadhar)
print("Multilevel inheritance")
c1=Citizen(45,"Jeevan","developer",209889873)
c1.getname()
c1.getage()
c1.getdesignation()
c1.getaadhar()
print("--------------------------------------")


#multiple inheritance
class Base1(object):  #object keyword is optional 
    age=10
    def __init__(self):
        self.var1="Base1 variable"

class Base2():
    age=20
    def __init__(self):
        self.var2="Base2 variable"

class Derived(Base1,Base2):
    def __init__(self):
        super().__init__() #should not put self in this init. 
                           #This is for calling the first base class constructor
        #Base1.__init__(self) #This can also be used to call the first base class constructor
        Base2.__init__(self) #This is for calling the second base class constructor
        print("Derived class")
print("multiple inheritance")
d1=Derived()
print(d1.var1)
print(d1.var2)
print(d1.age) #this will print the first base class age as it has higher priority
print("--------------------------------------")


#Hierarchial inheritance
class A():
    a=10

class B1(A):
    def __init__(self):     #parent class constructor will be called implicitly
        print(self.a)

class B2(A):
    def __init__(self):
        print(self.a)

print("hierarchial inheritance")
B1()
B2()
print("--------------------------------------")

'''
Output:

simple example
I'm Child! I'm having 100 Lakhs
I'm Parent! I'm having 600 Lakhs
--------------------------------------
base class
name: Karthi
age: 19
--------------------------------------
single level inheritance
name: Lokesh
age: 23
designation: Manager
--------------------------------------
Multilevel inheritance
name: Jeevan
age: 45
designation: developer
aadhar: 209889873
--------------------------------------
multiple inheritance
Derived class
Base1 variable
Base2 variable
10
--------------------------------------
hierarchial inheritance
10
10
--------------------------------------
'''