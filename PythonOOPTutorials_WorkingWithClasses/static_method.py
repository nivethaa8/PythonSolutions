class Employee:

    num_of_emps=0
    raise_amt=1.04

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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    ### Using a static method to see if a particular day was a work day. This does not directly impact the program
    #But it is in some day relevent, so you can use a static method

    @staticmethod
        #Can automatically pass in anything you want to work in first
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))


print(num_of_emps)