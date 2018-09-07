# Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value.
#
# As they enter each topping, print a message saying you'll add that topping
# to their pizza.

new_topping = ''

while new_topping != 'quit':
    new_topping = input("Enter your choice of topping:\n ")
    message = "We will add that topping to your pizza."
    print(message)
