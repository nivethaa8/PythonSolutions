class Email:

    def __init__(self):
        self.is_sent = False
    def send_email(self):
        self.is_sent = True

#Create an object = to Email()
my_email = Email()

#Class.attribute init so automatically called without self
print(my_email.is_sent)

#Object.function() ==> Call the function to validate the function itself
my_email.send_email()
#Object.attribute
#Not object.attribute(args) because there are no args
print (my_email.is_sent)


