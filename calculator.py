try:
    # take input of first number from user
    num1 = float(input("Enter first number:"))
    # take input of any one opertaion from user
    oper = input("select any one operator (+, -, *, /): ")
    # take input of second number from user
    num2 = float(input("Enter second number:"))

    # addition
    if oper == "+":
        result = num1 + num2    # addition of num1 and num2 and store result in result variable
        print("Answer: ", result)  #print result

    # subtraction
    elif oper == "-":
        result = num1 - num2  # subtraction of num1 and num2 and store result in result variable
        print("Answer: ", result)

    # multiplication
    elif oper == "*":
        result = num1 * num2    # multiplication of num1 and num2 and store result in result variable
        print("Answer: ", result)

    # division
    elif oper == "/":
        # check num2 value if it not zero then go in if statement if value is zero go in else
        if num2 != 0: 
            result = num1/num2   # division of num1 and num2 and store result in result variable
            print("Answer: ",result)
        else: 
            print("Error: Division by zero is not allowed.")

    else: 
        print("Invalid operator!")

except ValueError:
    print("Invalid Input / Enter numeric value")