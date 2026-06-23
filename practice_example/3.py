# Question 3: Grade Calculator 
# Question: Write a program that takes a student's marks and prints the grade using the following conditions: 
# ● 90 and above → A 
# ● 75 to 89 → B 
# ● 50 to 74 → C 
# ● Below 50 → Fail 

try:
    mark = int(input("Enter marks:"))
    if mark >= 90:
        print("A Grade!")
    elif mark >= 75:
        print("B Grade!")
    elif mark >= 50:
        print("C Grade!")
    else:
        print("Fail")
except ValueError:
    print("Invalid number!")