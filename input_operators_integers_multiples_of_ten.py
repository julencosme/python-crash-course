# Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Enter a number, and I'll tell you if it is a multiple of ten or not: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is a multiple of ten.")
else:
    print("The number " + str(number) + " is not a multiple of ten.")

    