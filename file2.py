# using dictionary
# inside constructor by using self variable
class Student:
    def __init__(self):
        self.id=101
        self.name="Bhushan Wagh"
        self.addr="Jalgaon city"
        self.course="Bachelor of Computer Application"
        self.fees=25600
       # print("\n",self.__dict__)
s=Student()
print(s.__dict__)