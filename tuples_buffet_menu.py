# Improved indentation style for this code in file: "indentation_style_buffet_menu.py".

buffet_foods = ('lo mein', 'crab legs', 'fried rice',
                'hot pepper fish stew', 'almond cookies')
print(buffet_foods)

# For loop to print food items the restaurant offers .

for foods in buffet_foods:
    print(foods)
for foods in buffet_foods:
    print(foods.title())


# Menu items change.
#
# Rewriting the tuple, and using a for loop to print each of the items on the
# revised menu .

buffet_foods = ('lo mein', 'crab legs', 'fried rice',
                'hot pepper fish stew', 'almond cookies')
print("Original Menu:")
for foods in buffet_foods:
    print(foods)
buffet_foods = ('lo mein', 'crab legs', 'white rice',
                'egg drop soup', 'almond cookies')
print("New Menu:")
for foods in buffet_foods:
    print(foods)
