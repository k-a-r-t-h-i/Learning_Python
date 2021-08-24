#Errors
#1. Syntax Error
#2. Logical Error
#Occurs all the time

#Exception
#an event that disrupts the flow of execution. 
#It may or may not occur all the time. I
#It occurs in specific senarios or specific inputs

def print_5th_element(L):
    try:
        print(L[4]) 
        #if any error happens in try block the control will be transferred to the except block
        print(L)
        #if there is any exception the execution of try block stops there itself and no other line in the try block gets executed
    except:
        print("Sorry you don't have sufficient elements!!")
        #executed when an exception occurs
    else:
        print("everything works fine")
        #executed when there is no exception
    finally:
        print("Thank you!!")
        #this block will be executed at any case

size=int(input("Enter the list size: "))
L=[]
for _ in range(0,size):
    L.append(int(input("Enter list element: ")))

print_5th_element(L)

"""
Output:
Enter the list size: 3
Enter list element: 1
Enter list element: 2
Enter list element: 3
Sorry you don't have sufficient elements!!
Thank you!!
"""


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a/b)
except ZeroDivisionError:
    print("Number cannot be divided by zero!!")
except ValueError:
    print("Give proper inputs!")
except:
    print("Something went wrong!!")

"""
Output:
Enter a number: 2
Enter a number: r
Give proper inputs!
"""