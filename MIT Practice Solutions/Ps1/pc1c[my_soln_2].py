starting_salary = int(input("What is your starting salary"))
months_salary = starting_salary/12
total_cost = 1000000
semi_annual_return = 0.07
r = 0.04
down_payment = 0.25*(total_cost)

epsilon = 100
steps = 0
low = 0
high = 10000
guess = (low+high)/2.0
saving_rate = guess/10000
current_savings_for_down_payment = 0
steps = 0


def calculations (saving_rate, starting_salary):
    current_savings_for_down_payment = 0
    for month in range (0,36):
            if (month % 6) == 1:
                starting_salary = starting_salary * (1 + semi_annual_return)

            monthly_salary_saved_for_down_payment = (saving_rate) * (starting_salary/12)
            ROI_for_down_payment = current_savings_for_down_payment * (r / 12)
            current_savings_for_down_payment = current_savings_for_down_payment + monthly_salary_saved_for_down_payment + ROI_for_down_payment

    return current_savings_for_down_payment

while abs(current_savings_for_down_payment - down_payment) > epsilon:
    current_savings_for_down_payment = calculations(saving_rate, starting_salary)

    if current_savings_for_down_payment > down_payment + epsilon:
        high = guess
        current_savings_for_down_payment = 0

    elif current_savings_for_down_payment < down_payment - epsilon:
        low = guess
        current_savings_for_down_payment = 0

    if steps > 100:
        break

    steps = steps + 1
    guess = (low + high) / 2.0
    saving_rate = guess / 10000


print ("Steps", steps)
print("Current Savings For Down Payment", current_savings_for_down_payment)
print("saving rate", saving_rate)


