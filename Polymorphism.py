#inbuilt polymorphism
print("inbuilt polymorphism")
# len() being used for a string
print(len("hello"))
 
# len() being used for a list
print(len([1,4,45]))

print("------------------------------------------------")

#user defined polymorphism
print("user defined polymorphism")
def mul(x,y=10):
    print(x*y)

mul(1,2)
mul(2)

print("------------------------------------------------")

#polymorphism in class
print("polymorphism in class")
class A():
    def a(self):
        print("A class")
class B():
    def a(self):
        print("B class")

A().a()
B().a()

print("------------------------------------------------")

#note on overriding
print("note on overriding")
def add(x,y,z=10):
    print(x+y+z)

def add(x,y):    #this over writes the previous add
    print(x+y)

add(1,2)
#add(1,2,3) there is no overriding in python so executing this will give error

print("------------------------------------------------")

'''
Output:
inbuilt polymorphism
5
3
------------------------------------------------
user defined polymorphism
2
20
------------------------------------------------
polymorphism in class
A class
B class
------------------------------------------------
note on overriding
3
------------------------------------------------
'''