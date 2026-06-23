def  Calculator(num1, oper, num2):
    try:

        if oper == "+":
            result = num1 + num2 
            print("Answer: ", result)  

        elif oper == "-":
            result = num1 - num2  
            print("Answer: ", result)

        elif oper == "*":
            result = num1 * num2  
            print("Answer: ", result)

        elif oper == "/":
            if num2 != 0: 
                result = num1/num2
                print("Answer: ",result)
            else: 
                print("Error: Division by zero is not allowed.")

        else: 
            print("Invalid operator!")

    except ValueError:
        print("Invalid Input / Enter numeric value")


result = Calculator(4, "+", 5)

