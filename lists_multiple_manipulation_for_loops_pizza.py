
# My Pizzas, Your Pizzas: Start with your pizza program from course.
# Make a copy of the list of pizzas, and call it friend_pizzas . 

favorite_pizzas= ['mushroom', 'tomato', 'artichoke', 'double-pepperoni']
friend_pizzas= favorite_pizzas[:]
print(favorite_pizzas)
print(friend_pizzas)

# Add a new pizza to the original list .

favorite_pizzas= ['mushroom', 'tomato', 'artichoke', 'double-pepperoni']
friend_pizzas= favorite_pizzas[:]
print(favorite_pizzas)
print(friend_pizzas)
favorite_pizzas.append("jalepeno")
print(favorite_pizzas)
print(friend_pizzas)

# Add a different pizza to the list friend_pizzas .

favorite_pizzas= ['mushroom', 'tomato', 'artichoke', 'double-pepperoni']
friend_pizzas= favorite_pizzas[:]
print(favorite_pizzas)
print(friend_pizzas)
favorite_pizzas.append("jalepeno")
print(favorite_pizzas)
print(friend_pizzas)
friend_pizzas.append("pineapple")
print(friend_pizzas)
print(favorite_pizzas)

# Prove that you have two separate lists . 
# Print the message, My favorite pizzas are:, and then use a for loop to print 
# the first list . 
#
# Print the message, My friend’s favorite pizzas are:, and then use a for loop 
# to print the second list . 
# 
# Make sure each new pizza is stored in the appropriate list .

print("My favorite pizzas are: ")
for pizza in favorite_pizzas[:]:
    print(pizza.title())

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas[:]:
    print(pizza.title())

# More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space . 
# 
# Choose a version of foods.py, and write two for loops to print each list
# of foods .

for pizza in friend_pizzas[:2]:
        print(pizza.title())
for pizza in favorite_pizzas[:3]:
    print(pizza.title())
for pizza in favorite_pizzas[:]:
    print(pizza.title())
for pizza in friend_pizzas[:]:
    print(pizza.title())

