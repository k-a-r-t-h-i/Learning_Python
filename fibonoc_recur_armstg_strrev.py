#fibonocci
def fibonocci(n):
    a=1
    b=1
    print(a,b,end=' ')
    for _ in range(8):
        temp=a
        a=b
        b+=temp
        print(b, end=' ')
fibonocci(8)

#prime number
def prime(n):
    for _ in range(2,n):
        if n%_ == 0:
            return False
    return True

print(prime(2))

#armstrong
def armstrong(n):
    tot=0
    for _ in str(n):
        tot+= int(_)**3
    if tot == n:
        return True
    else:
        return False
print(armstrong(153))

#reverse a string using recursion
def string_reverse(s):
    if len(s)==1:
        return s
    else:
        return s[len(s)-1] + string_reverse(s[:(len(s)-1)]) 

print(string_reverse('myname'))

def string_reverse(s):
    if len(s)==1:
        return s
    else:
        return string_reverse(s[1:])+s[0]

print(string_reverse('keerthi'))