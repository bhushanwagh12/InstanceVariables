# instance variables using a constructor

class Employee:
    def __init__(self):
        self.id=101
        self.name="bhushan"
        self.desg="software Engineer"
        self.sal=25450
        self.phno=9834101934
        self.email="bhushan123@gmail.com"
        self.domain="www.github.com/bhushanwagh12"
    def emp(self):
        print("Employee ID :\t",self.id)
        print("Name        :\t",self.name)
        print("Designation :\t",self.desg)
        print("Salary      :\t",self.sal)
        print("phone no    :\t",self.phno)
        print("Email       :\t",self.email)
        print("Domain Name :\t",self.domain)
c=Employee()
c.emp() 