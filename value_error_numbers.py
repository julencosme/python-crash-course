# Prompting for two numbers and then adding them together.
# Catching the 'ValueError' if a non-numerical character is used for input.

try:
    first_number = input("\nFirst number: ")
    second_number = input("second number: ")

    answer = int(first_number) + int(second_number)
    print(answer)
except ValueError:
    print("You have entered a non-numerical input value.")
