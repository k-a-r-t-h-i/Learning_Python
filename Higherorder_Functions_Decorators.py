#Higher order functions
print("Higher order functions")

def sum(n,func):
    total=0
    for i in range(1,n+1):
        total+=func(i)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(3,cube))       #note: the 2nd argument is a function reference not string
print(sum(3,square))
print()

#decorators
print("Decorators")
print("Decorators without parameters")
def be_polite(fn):
    def wrapper():
        print("Hello, pleasure to meet you")
        fn()
        print("Have a great day")
    return wrapper

@be_polite
def greet():
    print("My name is Karthi")

@be_polite
def rage():
    print("I Hate you")

greet()
rage()
print()

print("Decorators with parameters")
def be_polite_parm(fn):
    def wrapper_parm(*args,**kwargs):
        print("Hello, pleasure to meet you")
        fn(*args,**kwargs)
        print("Have a great day")
    return wrapper_parm

@be_polite_parm
def greet_parm(k,i,j):
    print("My name is Karthi",i,j)

@be_polite_parm 
def rage_parm():
    print("I Hate you")

greet_parm(4,j=2,i=7)
rage_parm()
print()

print("Real use case")  #parameter validation
def be_polite_real(fn):
    def wrapper_real(*args):
        if type(args) == int:
            print("Hello")
            fn(*args)
            print("Have a great day")
        else:
            print("invalid arguments")
    return wrapper_real

@be_polite_real
def greet_real(*args):
    print("My name is Karthi",args)


greet_real("kar",2,7)
print()

"""
Output:

Higher order functions
36
14

Decorators
Decorators without parameters
Hello, pleasure to meet you
My name is Karthi
Have a great day
Hello, pleasure to meet you
I Hate you
Have a great day

Decorators with parameters
Hello, pleasure to meet you
My name is Karthi 7 2
Have a great day
Hello, pleasure to meet you
I Hate you
Have a great day

Real use case
invalid arguments

"""