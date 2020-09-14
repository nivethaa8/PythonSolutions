class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):

        #Both can be used to access parent class data
        #Let the parent class deal with first, last, pay
        #This new method will only deal with pay
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang

class Manager(Employee):

    #Need to pass in list of employees that this manager supervises

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print ('-->', emp.fullname())




# dev_1 = Employee('Corey', 'Schafer', 50000)
# dev_2 = Employee('Test', 'Employee', 60000)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000,'Java')

mgr_1 = Manager ('Sue', 'Smith', 90000, [dev_1])
##Dev 1 represents the first developer

print (type(dev_1))

print(Employee.raise_amt)
print(dev_1.raise_amt)
print(dev_2.raise_amt)
print(mgr_1.raise_amt)

print(Developer.raise_amt)
print(dev_1.raise_amt)
print(dev_2.raise_amt)
print(mgr_1.raise_amt)

print("###Start of Extra Information###")

#Built-in funciton

print (isinstance(mgr_1, Manager))
print (isinstance(mgr_1, Employee))
print (isinstance(mgr_1, Developer))

print (issubclass(Developer, Employee))
#will tell us if a class is a subclass of another#
print (issubclass(Manager, Employee))
print (issubclass(Developer, Manager))




print("###End of Extra Information###")

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print("###")
#This gives information about the RUN outcome
# print(help(Developer))

print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)