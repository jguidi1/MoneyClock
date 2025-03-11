import time

def salary_to_hourly(salary):
    wage_per_second(salary / 2080)

def wage_per_second(hourly_wage):
    clock(hourly_wage / 3600)

def clock(cost):
    wage = 0 # The amount of money earned
    # Loop from 0 to 60 and print each number
    for number in range(61):
        wage += cost
        print(f"In this many seconds: {number}, You have made: ${wage:.2f}")
        time.sleep(1)
    
user_choice = input("Enter S for Salary or H for Hourly: ")
if user_choice == 'S':
    user_value = float(input("Enter your salary: "))
    salary_to_hourly(user_value)
else:
    user_value = float(input("Enter your hourly wage: "))
    wage_per_second(user_value)

