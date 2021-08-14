#iterartor
#used with iterable objects like string , list,.....
print("Iterator")
s='Dog'

i=iter(s)       #creating iterartor

print(next(i))          # to get next next values
print(next(i))
print(next(i))          #when exceeds string size it gives error

s=[1,2,3]
i=iter(s)
print(next(i))
print(next(i))
print(next(i))
print()

import sys

#getsizeof()
#getsizeof() returns the size occupied in RAM in bytes,
#can be used with any varable eg:
print("getsizeof()")

print(sys.getsizeof([1,7,9.078,'kjah',[1,9,8]]))
print()

#list comprehension
print("list comprehension")

list_comp = sys.getsizeof([i*10 for i in range(1000)])
#[i*10 for i in range(1000)] => this is the list comprehension
print(list_comp)
print()

#generators
#high speed ,less memory when compared to list comprehension
print("generator")

gen_comp = sys.getsizeof(i*10 for i in range(1000))
#i*10 for i in range(1000) => this is the list comprehension
print(gen_comp)
print()

#generator can be created in two ways
#1st way
print("1st way")

#for i in range(10):
#   if i%2==0:
#       print(i)
#this for loop can be written in a single line

gen_obj=(i for i in range(10) if i%2==0)
#i for i in range(10) if i%2==0 this syntax is also used for set and list comprehension
print(gen_obj)  #this just tells the object type

#we have to extract data by typecasting to list tuple or set(same as list without duplicates)
print(list(gen_obj)) #use this or 
#r=iter(gen_obj)
#print(next(r))
#print(next(r))
#print(next(r))
#print(next(r))
print()

#2nd way
print("2nd way generator function")

#generator function can be treated like an iterable object
def gen_fun():
    for i in range(10):
        if i==0:
            yield f"{i} is zero"     #yield internally acts as return but it remembers last line of execution in previous call
        if i%2 ==0:
            yield f"{i} is even"
        else:
            yield f"{i} is odd"
print(gen_fun())
#we can use iterator to call or use a for loop
for val in gen_fun():
    print(val)
print()

#this is the normal fuction observe the difference in output
print("normal function")
def nrml_fun():
    for i in range(10):
        if i==0:
            return f"{i} is zero"     
        if i%2 ==0:
            return f"{i} is even"
        else:
            return f"{i} is odd"
for val in range(10):
    print(nrml_fun())
print()

'''
Output:
Iterator
D
o
g
1
2
3

getsizeof()
56

list comprehension
4516

generator
64

1st way
<generator object <genexpr> at 0x08F30>
[0, 2, 4, 6, 8]

2nd way generator function
<generator object gen_fun at 0x01BC0>
0 is zero
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd

normal function
0 is zero
0 is zero
0 is zero
0 is zero
0 is zero
0 is zero
0 is zero
0 is zero
0 is zero
0 is zero

'''
