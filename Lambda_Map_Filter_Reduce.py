#lambda function (otherwise anonymous function => it doesn't have a name)

#this is a normal function
print("normal function")
def fun():          #dir(fun) can be used to identify available methods
    pass
print(fun.__name__)
print()

#lambda function
print("lambda function")
#conditions:
#1. It should have only one line of execution
#2. the one line of execution should be return statement
#3. It must have a single parameter
#syntax: function-object = lambda parameter: return_statement
#return_statement should not have return keyword just the statement it returns implicity

sqr_fun= lambda x: x*x
print(sqr_fun.__name__)
print(sqr_fun(2))

area= lambda x,y: x*y
print(area(3,4))

vol= lambda x,y,z: x*y   #though we are not using Z this executes fine
print(vol(3,4,9))

# map, filter, reduce can be only used with iterable objects

#map function
print("map")
#it is used when a function has to be applied for all the elements in the iterable object
#syntax: map_object = map(function_name, iterable_object)
fun = lambda x: x*x
ls=[1,2,3,4,5,6,7]
map_obj = map(fun,ls)
print(map_obj)
print(list(map_obj))
#once data is extracted from map object, data gets vanished (this applies for filter too)
print(list(map_obj))
print()

#filter
print("filter")
#it's used to filter some elemnts based on some condition given in the function
#function should return only boolean and should have only one parameter
#syntax: filter_object = filter(function_name, iterable_object)
fun = lambda x: x%2==0
filter_obj = filter(fun,ls)
print(filter_obj)
print(list(filter_obj))
print(list(filter_obj)) #this will be empty as it is already extracted

#reduce
print("reduce")
#the function should have more than one parameter
from functools import reduce  #reduce is in this module not inbuilt
#what it does?
#it takes the initial value of the parameters from the iterable object
#in next next iteration the first parameter wolud be the
#output from previos ietration the others parameters gets values
#from the iterable object
#syntax: reduce_object = reduce(function_name, iterable_object)
fun= lambda x,y: x+y 
s=[1,2,3,4,5,6,7]
reduce_obj = reduce(fun,s)
#here x and y takes first 2 values from s (ie. 1,2) adds(3) it
#and stores it in x for 2nd iteration x has previous output
#and y takes 3rd value from s (now: x=3,y=3)
#it proceeds in this way until all elements are processed
print(reduce_obj) #no need of type casting for reduce
print(reduce_obj) #data doesn't get vanished in reduce

"""
Output:

normal function
fun

lambda function
<lambda>
4
12
12
map
<map object at 0x00F70950>
[1, 4, 9, 16, 25, 36, 49]
[]

filter
<filter object at 0x00F70AB0>
[2, 4, 6]
[]
reduce
28
28
"""