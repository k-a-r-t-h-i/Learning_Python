#Property Decorator
    #Setter
    #Getter

class Student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    @property               #Getter
    def _name(self):
        return self.name
    @_name.setter           #Setter
    def _name(self,name):
        if self.gender=="Male":
            self.name= "Mr."+ name
        else:
            self.name= "Ms."+ name
student_1=Student("ABC","Male")
student_1._name="ABC"
student_2=Student("XYZ","Female")
student_2._name="XYZ"
print(student_1._name)
print(student_2._name)

"""
Output:

Mr.ABC
Ms.XYZ

"""