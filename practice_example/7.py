# Question 7: Function with Multiple Parameters 
# Question: Create a function calculate_salary(basic, hra, bonus) that returns the total salary. Take the three values as input and print the result. 

def calculate_salary(basic, hra, bonus):
    total = basic + hra + bonus
    return total
    
try:
    basic = float(input("Enter basic salary:"))
    hra = float(input("Enter HRA:"))
    bonus = float(input("Enter bonus:"))

    result = calculate_salary(basic, hra, bonus)    
    print(f"Total Salary: {result:.2f}" )
except ValueError:
    print("Invalid Input! Please enter numeric values.")
