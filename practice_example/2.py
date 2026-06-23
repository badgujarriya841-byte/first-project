# Question 2: Type Casting and Average 
# Question: Take three numbers as input (they may contain decimal values). Convert them to float using type casting and print their average rounded to 2 decimal places. 

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

avg = (a + b + c)/3

print(f"Average: {avg:.2f}")