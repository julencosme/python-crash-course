# Shrinking Guest List: You just found out that your new dinner table won't
# arrive in time for the dinner, and you have space for only two guests.
#
# Start with your program from Exercise 3-6 . Add a new line that prints a
# message saying that you can invite only two people for dinner.
#
# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a message
# to that person letting them know you're sorry you can't invite them to dinner.
#
# Print a message to each of the two people still on your list, letting them
# know they're still invited.
#
# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program .

guests = ['Uncle J', 'Jo', 'Jon', 'Jill']
message = ", please join me for dinner."
print(guests)
print(message)

# Adding elements to the list
print((guests[0]) + message)
print((guests[1]) + message)
print((guests[2]) + message)
print((guests[3]) + message)

# Add one more guest
guests.append('Mom')
print(guests)

# Print message with new guest list
print((guests[4]) + message)

# Use insert() to add more guests
guests.insert(0, 'Jerry')
print(guests)
guests.insert(2, 'John')
print(guests)

# Use append() to add two more guests
guests.append('Franklin')
guests.append('Dad')
print(guests)

# Print message with new guest list
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
#
# Shrinking Guest List: You just found out that your new dinner table won't
# arrive in time for the dinner, and you have space for only two guests.
#
# Start with your program from Exercise 3-6 . Add a new line that prints a
# message saying that you can invite only two people for dinner.

message = "I can only invite two people for dinner."
print(message)

# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a message
# to that person letting them know you're sorry you can't invite them to dinner.
#
# Print a message to each of the two people still on your list, letting them
# know they're still invited.
#
# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

# Print list to see entire guest list
print(guests)
# Add a new message letting guests know that they are not invited
message = ", I regret to inform you that I can no longer extend an invitation to dinner."

# Use pop() to remove guests from lists
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


# Print new guest list
print(guests)

# Print new message to the two invites
message = ", you are still invited to dinner."
print((guests[0]) + message)
print((guests[1]) + message)

# Del guests[0, -1] to remove all elements/guests
del guests[0]
del guests[-1]

# Check to make sure your list is empty
print(guests)
