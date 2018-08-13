# Working with Tuples
#
# Buffet: A buffet-style restaurant offers only five basic foods . 
# Think of five simple foods, and store them in a tuple .
#
# Improved indentation style for this code in file: "indentation_style_buffet_menu.py".

buffet_foods= ('lo mein', 'crab legs', 'fried rice', 'hot pepper fish stew', 'almond cookies')
print(buffet_foods)

 # Use a for loop to print each food the restaurant offers .

for foods in buffet_foods:
    print(foods)
for foods in buffet_foods:
    print(foods.title())

# Try to modify one of the items, and make sure that Python rejects the change .
#
# This section of code (below) is commented out, so as not to get confused with error output
# (since that is the objective of this section of the exercise).

# buffet_foods.insert(0, 'hot and sour soup')
# print(buffet_foods)

# The restaurant changes its menu, replacing two of the items with different foods. 
# 
# Add a block of code that rewrites the tuple, and then use a for loop
# to print each of the items on the revised menu .

buffet_foods= ('lo mein', 'crab legs', 'fried rice', 'hot pepper fish stew', 'almond cookies')
print("Original Menu:")
for foods in buffet_foods:
    print(foods)
buffet_foods= ('lo mein', 'crab legs', 'white rice', 'egg drop soup', 'almond cookies')
print("New Menu:")
for foods in buffet_foods:
    print(foods)
    
