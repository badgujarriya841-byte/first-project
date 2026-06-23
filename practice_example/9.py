# Question 9: Student Result Analyzer 
# Question: Create a function calculate_result(mark1, mark2, mark3) that returns: 
# ● "Distinction" if average ≥ 75 
# ● "First Class" if average ≥ 60 and < 75 
# ● "Second Class" if average ≥ 40 and < 60 
# ● "Fail" if average < 40 
# Use exception handling to ensure all marks are between 0 and 100. If any mark is invalid, print "Invalid Marks". 

def calculate_result(mark1, mark2, mark3):
    if not (0 <= mark1 <=100 and 0 <= mark2 <=100 and 0 <= mark3 <=100):
        raise ValueError("Invalid marks")

    average = (mark1 + mark2 + mark3)/3

    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Class"
    elif average >= 40:
        return "Second Class"
    else:
        return "Fail"
    
try:
    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))

    result = calculate_result(mark1, mark2, mark3)
    print(result)

except ValueError:
    print("Invalid Marks")       