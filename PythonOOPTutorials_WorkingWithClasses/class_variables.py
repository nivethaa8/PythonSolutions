class Employee:
    raise_amount = 1.09
    num_of_empls = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

        Employee.num_of_empls += 1
        #Don't use self here because the total number doesn't change per creation of an instance


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #works
        # self.pay = int(self.pay * Employee.raise_amount)
        #works, use this because this can be applied to any instance
        self.pay = int(self.pay * self.raise_amount)

        # self.pay = int(self.pay * raise_amount) -> Can not use this because of how to access class variables

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.raise_amount = 1.09
#This will change it for all instances

emp_1.raise_amount = 1.06
#This will only change it for that specified instance

print (Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_empls)
print(emp_1.fullname())



