# import calculate_power from funcPower.py file

from funcPower import calculate_power

try:
    base = int(input("Enter base number: "))
    exponent = int(input("Enter exponent number: "))

    result = calculate_power(base, exponent)
    print("Power of", base,"^",exponent, "is", result)

except ValueError as e:
    print(e)