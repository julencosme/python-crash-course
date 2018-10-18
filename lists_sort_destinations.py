# List in original order.
vacation_destinations = ['Scandinavia', 'France', 'Russia', 'Guam', 'Colombia']
print(vacation_destinations)

# List in alphabetical order, without modifying the actual list.
print(sorted(vacation_destinations))
print(vacation_destinations)

# List in reverse alphabetical order, without changing order of the original list .
print(sorted(vacation_destinations, reverse=True))
print(vacation_destinations)

# Reverse() to change order of list.
vacation_destinations.reverse()
print(vacation_destinations)

# Reverse() to change order of list -- again -- list now in its original order.
vacation_destinations.reverse()
print(vacation_destinations)

# Sort() to change list and store list in alphabetical order.
vacation_destinations.sort()
print(vacation_destinations)

# Sort() to change list and store list in reverse alphabetical order.
vacation_destinations.sort(reverse=True)
print(vacation_destinations)
