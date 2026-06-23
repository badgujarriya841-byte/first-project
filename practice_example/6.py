# Question 6: Safe Integer Conversion 
# Question: Take a value as input and convert it into an integer using type casting. If the conversion fails, handle the exception and print "Invalid Input". 

try:
    num = (input("enter number:"))
    result = int(num)
    print(num)
except ValueError:
    print("Invalid Input!")