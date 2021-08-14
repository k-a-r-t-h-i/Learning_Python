#Functions / methods
# is an independent block of code

#function creation

def add(a,b):
    c=a+b
    print(c)

#calling a function
add(3,5)

def add(a,b):
    c=a+b
    return c

result=add(45,-123)
print(result)


def dummyfunction():
    a=1
#returns None as there is no return type

print(dummyfunction())


"""
Example:
Passkey generator
1. Extract length
2. Extract Year of birth
3. Sum of DOB.
"""
def extract_length_of_ename(ename):
    length = len(ename)
    return length



def extract_yob(dob):
    yob = dob.split("-")[2]
    return yob



def sum_of_dob(dob):
    output = 0
    for i in dob:
        if i!="-":
            output = output + int(i)
    return output



def compute_secret_key(ename, dob):
    a = extract_length_of_ename(ename)
    b = extract_yob(dob)
    c = sum_of_dob(dob)
    return str(a) + "" + str(b) + "" + str(c)

result = compute_secret_key("Hunt","13-03-1994")
print(result)

'''
Output:
8
-78
None
4199430
'''