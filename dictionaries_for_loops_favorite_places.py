favorite_places = {
    'lionel': ['arcata', 'bellingham', 'las cruces'],
    'jorge': ['paris', 'germany', 'washington'],
    'bella': ['guam', 'las vegas', 'virginia beach'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
