# Favorite Places: Make a dictionary called favorite_places.
#
# Think of three names to use as keys in the dictionary, and store one 
# to three favorite places for each person.
# 
# Loop through the dictionary, and print each person's name and
# their favorite places.

favorite_places = {
    'lionel': ['arcata', 'bellingham', 'las cruces'],
    'jorge': ['paris', 'germany', 'washington'],
    'bella':['guam', 'las vegas', 'virginia beach'],
    }

for name, places in favorite_places.items():
  print("\n" + name.title() + "'s favorite places are:")
  for place in places:
    print("\t" + place.title())