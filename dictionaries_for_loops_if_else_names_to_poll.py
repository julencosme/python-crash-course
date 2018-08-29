# Polling: Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not.

# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll .

favorite_languages = {
    'jen': 'python',
    'sci': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'tanya': 'elixir', 
    'miles': 'python',
    'jill': 'clojure',
    }

names_to_poll = ['jill', 'miles', 'tanya', 'emily', 'susanne']

for name in names_to_poll:
    if name in favorite_languages:
        print("Thank you for participating in our poll.")
    else:
        print("Hi, " + name.title() + " please take our poll.")
        