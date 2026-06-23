# Question 8: Employee Bonus Calculator 
# Question: Create a function calculate_bonus(salary, experience) that calculates an employee's bonus based on the following conditions: 
# ● Experience ≥ 10 years → 20% of salary 
# ● Experience ≥ 5 years and < 10 years → 10% of salary 
# ● Experience < 5 years → 5% of salary 
# Print the bonus amount. 

def calculate_bonus(salary, experience):
    if experience >= 10:
        bonus = salary * 0.20
    elif experience >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    
    return bonus

try:
    salary = float(input("Enter your salary:"))
    experience = int(input("Enter years of experience:"))

    bonus = calculate_bonus(salary, experience)
    print("Bonus:", bonus)

except ValueError:
    print("Invalid Input! Please enter numeric values.")

    