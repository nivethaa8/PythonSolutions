num = input ("Enter a 3 digit number ")
first_digit = (num //100)
second_digit =  ((num //10) % 10)
third_digit = (num%10)

sum = first_digit + second_digit + third_digit

print ("The sum of the digits is %d" % (sum))
