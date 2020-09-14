#Python Object - Oriented Programming

# Data and functions associated with class, called attributes and methods
# methods are functions associated with a classs

class Employee:

    def __init__(self,first,last,pay):
        #these are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +  '.' + last + '@gmail.com'

    #this is a method
    def fullname(self):
        return '{} {}'.format (self.first, self.last)

    def apply_raise (self):
        self.pay = int(self.pay * 1.04)


#Each method within a class takes instance as first argument which is always self
#Instance is only argument you need to get full name

# Class - blueprint for creating instance

# Instance variable contain data specific to each instance

emp_1 = Employee('Corey', 'Shah', 50000)
#emp1 would be self
emp_2 = Employee('Test', 'Wonder', 60000)

# print (emp_1)
# print (emp_2)

print(emp_1.email)
print (emp_2.email)
print (emp_1.fullname())
emp_1.apply_raise()
print(emp_1.pay)

