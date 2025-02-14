class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee ('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)
# print(emp_1.pay + emp_2.pay)
#
# print(1+2)
# #same as print(int.__add(1,2))
# print('a' + 'b')

##len is also a special function that runs in the background

print(len('test'))
print('test'.__len__())
print(len(emp_1))



print(emp_1)
print(repr(emp_1))
#same as emp_1.__repr__()
print(str(emp_1))
#same as emp_1.__str__()