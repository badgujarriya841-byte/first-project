#  Question 1: Largest of Three Numbers
#  Question: Write a program that takes three integers as input and prints the largest among them using conditional statements. 

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b and a > c:
    print("first number ",a, "is largest number!")
elif b > a and b > c :
    print("second number ",b, "is largest number!")
else: 
    print("third number ",c, "is largest number!")