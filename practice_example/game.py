import random
random_number = random.randint(1, 100)
print(random_number)

while True:
    try:
        user_num = int(input("Guess a number between 1 and 100: "))

        if user_num > random_number:
            print("Number is greater than the actual number! Try again.")
        elif user_num < random_number:
            print("Number is lower than the actual number! Try again.")
        else:
            print("You guessed the correct number! Congrats!")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")