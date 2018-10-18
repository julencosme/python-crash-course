favorite_pizzas = ['mushroom', 'tomato', 'artichoke', 'double-pepperoni']
friend_pizzas = favorite_pizzas[:]
print(favorite_pizzas)
print(friend_pizzas)

# Adding a new pizza to the original list .

favorite_pizzas = ['mushroom', 'tomato', 'artichoke', 'double-pepperoni']
friend_pizzas = favorite_pizzas[:]
print(favorite_pizzas)
print(friend_pizzas)
favorite_pizzas.append("jalepeno")
print(favorite_pizzas)
print(friend_pizzas)

# Adding a different pizza to the list friend_pizzas .

favorite_pizzas = ['mushroom', 'tomato', 'artichoke', 'double-pepperoni']
friend_pizzas = favorite_pizzas[:]
print(favorite_pizzas)
print(friend_pizzas)
favorite_pizzas.append("jalepeno")
print(favorite_pizzas)
print(friend_pizzas)
friend_pizzas.append("pineapple")
print(friend_pizzas)
print(favorite_pizzas)


print("My favorite pizzas are: ")
for pizza in favorite_pizzas[:]:
    print(pizza.title())

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas[:]:
    print(pizza.title())

# Two for loops to print each list of foods .

for pizza in friend_pizzas[:2]:
    print(pizza.title())
for pizza in favorite_pizzas[:3]:
    print(pizza.title())
for pizza in favorite_pizzas[:]:
    print(pizza.title())
for pizza in friend_pizzas[:]:
    print(pizza.title())
