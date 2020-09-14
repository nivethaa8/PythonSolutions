class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # 4. Create a property deconator
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname (self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        #set employee's new names to first and last
        self.first = first
        self.last = last

    #To create a deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    #call as del.fullname()

emp_1 = Employee('John', 'Smith')
#5. To do this we have to create a setter
emp_1.fullname = 'Corey Shafer'


#This is not a problem for fullname because fullname() is a function and recalling
#the fullname function which initalizes self.first and self.las
# emp_1.first = "Jim"


print(emp_1.fullname)

print(emp_1.first)
print(emp_1.email)
# #This is not the best choice
# print(emp_1.email())

#1. People do not want to change the email to email() everytime they change the first name and last name
#2. Update email automatically when name is changed - should not create a new function because
#it will break code for everyone using teh attributes of the class
#3. Use @property to us to define a method but we can access it as an attribute

del emp_1.fullname