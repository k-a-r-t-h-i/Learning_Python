"""
Types of variables
    -Local Variables (created within methods)
    -Instance Variables (created with self)
    -Class Variables (created within classes without self)
"""

class student:
    college_no="XYZ"    #class variables
    def __init__(self,stu_name):
        self.stu_name=stu_name  #Instance variables
        a=5         #Local Variables

obj=student("Karthi")
print(obj.stu_name)
print(obj.college_no)
print(student.college_no)       #class variables can be accessed with class name
                                #class variables have same value for any object 
                                #change in class variable affect it's value for all variables

"""
Output:
Karthi
XYZ
XYZ
"""