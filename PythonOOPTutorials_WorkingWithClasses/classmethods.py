class Employee:

    num_of_emps=0
    raise_amt=1.06

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps +=1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

#Create a classmethod when it is a request that forms a new use case
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        #The cls = Employee

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(Employee.fullname(emp_1))
### Class Methods ###
###Datetime.py also use class constructors
print(Employee.raise_amt)
Employee.set_raise_amt(1.09)
#This is a class method
#This is the same as Employee.raise_amt = 1.05

print(Employee.raise_amt)

print(emp_1.raise_amt)
print(emp_2.raise_amt)
emp_1.set_raise_amt(1.05)

#Doing this also works, but nobody changes a class variable via an instance



#Class methods as alternative constructors
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)

#How to split the emp_str_1 and use it without a function
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)
