# Modifying 'value_error_numbers.py' program.
# Using a while loop so that the user can continue to enter numbers even if
# they make a mistake by entering a non-numerical input value.


print("Enter two numbers, and we will add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You have entered a non-numerical input value.")
    else:
        print(answer)
