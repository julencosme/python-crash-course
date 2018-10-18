guests = ['Uncle J', 'Jo', 'Jon', 'Jill']
message = ", please join me for dinner."
print(guests)
print(message)

# Adding elements to the list
print((guests[0]) + message)
print((guests[1]) + message)
print((guests[2]) + message)
print((guests[3]) + message)

# Adding one more guest
guests.append('Mom')
print(guests)

# Printing message with new guest list
print((guests[4]) + message)

# Using insert() to add more guests
guests.insert(0, 'Jerry')
print(guests)
guests.insert(2, 'John')
print(guests)

# Using append() to add two more guests
guests.append('Franklin')
guests.append('Dad')
print(guests)

# Printing message with new guest list
print((guests[0]) + message)
print((guests[1]) + message)
print((guests[2]) + message)
print((guests[3]) + message)
print((guests[4]) + message)
print((guests[5]) + message)
print((guests[6]) + message)
print((guests[7]) + message)
print((guests[8]) + message)


# Remvoing elements from the list
message = "I can only invite two people for dinner."
print(message)


# Printing list to see entire guest list
print(guests)
# Adding a new message letting guests know that they are not invited
message = ", I regret to inform you that I can no longer extend an invitation to dinner."

# Using pop() to remove guests from lists
popped_guest_0 = guests.pop(0)
print((popped_guest_0) + message)
print(guests)

popped_guest_1 = guests.pop(0)
print((popped_guest_1) + message)
print(guests)

popped_guest_2 = guests.pop(0)
print((popped_guest_2) + message)
print(guests)

popped_guest_3 = guests.pop(0)
print((popped_guest_3) + message)
print(guests)

popped_guest_4 = guests.pop(0)
print((popped_guest_4) + message)
print(guests)

popped_guest_5 = guests.pop(0)
print((popped_guest_4) + message)
print(guests)

popped_guest_6 = guests.pop(0)
print((popped_guest_5) + message)
print(guests)


# Printing new guest list
print(guests)

# Printing new message to the two invites
message = ", you are still invited to dinner."
print((guests[0]) + message)
print((guests[1]) + message)

# Deleting guests[0, -1] to remove all elements/guests
del guests[0]
del guests[-1]

# Checking to make sure list is empty
print(guests)
