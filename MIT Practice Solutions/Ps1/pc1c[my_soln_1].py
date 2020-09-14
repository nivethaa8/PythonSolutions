r = 0.04
total_cost = 1000000
portion_down_payment = 0.25*(total_cost)
semi_annual_return = 0.07
epsilon = 100



def calculate(salary):
    #Here salary is mapped to starting_salary
    #SALARY itself is a number
    #Starting_Salary is a parameter

    steps = 0
    low = 0
    high = 10000

    while True:
        guess = (low + high) / 2
        saving_rate = guess / 10000
        steps = steps + 1
        current_savings_for_down_payment = 0
        starting_salary = salary
        #Must assign the salary parameter to another variable

        for month in range (36):
            if (month % 6) == 0:
                starting_salary = starting_salary * (1 + semi_annual_return)
                #NUMBER is not reassigned to another number
                #A VARIABLE must be reassigned to another number

            monthly_salary_saved_for_down_payment = (saving_rate) * (starting_salary/12)
            ROI_for_down_payment = current_savings_for_down_payment * (r / 12)
            current_savings_for_down_payment = current_savings_for_down_payment + monthly_salary_saved_for_down_payment + ROI_for_down_payment

        if (portion_down_payment - epsilon) <= current_savings_for_down_payment <= (portion_down_payment + epsilon):
            print("Saving Rate", saving_rate)
            print("Current Savings", current_savings_for_down_payment)
            print(steps)
            return

        if current_savings_for_down_payment > portion_down_payment + epsilon:
            high = guess

        elif current_savings_for_down_payment < portion_down_payment - epsilon:
            low = guess


        #Bisection max
        if steps > 14:
            print("Not possible")
            return

salary = int(input("What is your starting salary"))
calculate(salary)
#Now salary is a number



