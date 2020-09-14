class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email=first + "." + last + "@company.name"


    def fullname(self):
    #Every method within a class, automatically takes the instance as the first argument
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("corey", "Schafer", 50000)
#self.first = emp_1.first
emp_2 = Employee("Test", "User", 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
#Here, don't need to pass anything in because self is automatially
#Passed in via emp_1

#Above is transformed into bottom and that's how it works
print(Employee.fullname(emp_1))
#Here, it does not know what instance to use so it must be passed


