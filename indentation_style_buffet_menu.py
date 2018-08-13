# Indentation
#
# Code Review: Choose three of the programs you’ve written in this chapter and 
# modify each one to comply with PEP 8: 
# 
# Use four spaces for each indentation level . 
# Use less than 80 characters on each line.
# Don’t use blank lines excessively in your program files.

buffet_foods= (
        'lo mein', 'crab legs', 'fried rice',
        'hot pepper fish stew', 'almond cookies'
        )
print(buffet_foods)

buffet_foods= (
        'lo mein', 'crab legs', 'fried rice',
        'hot pepper fish stew', 'almond cookies'
        )
print("Original Menu:")
for foods in buffet_foods:
    print(foods)
buffet_foods= (
        'lo mein', 'crab legs', 'white rice',
        'egg drop soup', 'almond cookies'
        )
print("New Menu:")
for foods in buffet_foods:
    print(foods)