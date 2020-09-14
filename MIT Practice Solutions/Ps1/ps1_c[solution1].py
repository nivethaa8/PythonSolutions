starting_salary = int(input("What is your starting salary"))
months_salary = starting_salary/12
total_cost = 1000000
semi_annual_rate = 0.07
investment_return = 0.04
down_payment = 0.25*(total_cost)
current_savings = 0

epsilon = 100
steps = 0
low = 0
high = 10000
guess = (low+high)/2.0
guess = guess/10000


def calSavings (current_savings, months_salary, guess):
    for months in range(0,36):
        if months % 6 == 1:
            months_salary = months_salary * (1+semi_annual_rate)
        current_savings = current_savings + (months_salary*guess)
        current_savings = current_savings * (1+0.04)

    return (current_savings)

while abs(current_savings - down_payment) >= epsilon:
    current_savings = calSavings(current_savings, months_salary, guess)
    if current_savings < down_payment - 100:
        low = guess
        current_savings = 0
    elif current_savings > down_payment + 100:
        high = guess
        current_savings = 0
    if (steps > 100):
        break
    guess = (low + high)/2
    steps = steps + 1

print("Best saving rate", guess)
print("With current Saving", current_savings)
print(steps)
