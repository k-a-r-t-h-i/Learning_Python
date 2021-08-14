#importing an other module example
print("importing an other module example")
print()
from mod1 import varmod1    #this is one way
print("1st way:",varmod1)
print()

from mod1 import *    #this can also be used so that the attributes can be used directly without module or package name
print("2nd way:",varmod1)   
print()

import mod1 #this is another way
print("3rd way:",mod1.varmod1)
print()

import mod1 as m    #this also a way
print("4th way:",m.varmod1)
print()


#when a module is imported it executes the file

#########################################################

#importing an other package example
print("importing an other package example\n")
#when a package is imported it executes the __init__ file

import pkg1
#when importing like this individual modules has to be imported in __init__ file
print("sys.path with the help of sys imported in __init__.py file\n",pkg1.sys.path)
#when importing a file the system checks for it in the directories in sys.path

print("\n printing a variable with package: ")
print(pkg1.modpkg2.varmodpkg2)

print()
from pkg1 import modpkg1,modpkg2
#when importing like this the __init__ file can be empty
print("imported by from:")
print(modpkg1.A.var) #here modpkg1 can be accessed directly as it is imported using from
print(modpkg2.varmodpkg2)

print("\n name mangling variable accessing\n")
#name mangling variable
a=modpkg1.A()
print(dir(a))
print(a._A__var)#this is how you access a mangling variable

'''
Output:

importing an other module example

this will be executed when this module is imported
1st way: this is a variable in mod1

2nd way: this is a variable in mod1

3rd way: this is a variable in mod1

4th way: this is a variable in mod1

importing an other package example

Package 1 is imported
sys.path with the help of sys imported in __init__.py file
 ['e:|docs|programs|Understanding Modules and Packages', 'C:|well|Program|Python|python3.zip']    

 printing a variable with package:
variable inside modpkg2 in pkg1

imported by from:
variable in class A
variable inside modpkg2 in pkg1

 name mangling variable accessing

['_A__var', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_var', 'var']
name mangling variable
'''