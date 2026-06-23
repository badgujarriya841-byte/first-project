# Question 5: Match Case - Month Days 
# Question: Using a match-case statement, print the number of days in a month based on the month number. 
# ● February → 28 
# ● April, June, September, November → 30 
# ● Remaining months → 31 

month = int(input("Enter month number (any from 1 to 12) : "))

if  month == 2:
    print("The number of days in this month is 28!")
elif month == 4 and 6 and 9 and 11:
    print("The number of days in this month is 30!")
elif month > 12 and month < 1:
    print("Invalid month number!")
else:
    print("The number of days in this month is 31!")