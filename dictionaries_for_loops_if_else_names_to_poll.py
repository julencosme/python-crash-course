favorite_languages = {
    'jen': 'python',
    'sci': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'tanya': 'elixir',
    'miles': 'python',
    'jill': 'clojure',
}

names_to_poll = ['jill', 'miles', 'tanya', 'eli', 'susanne']

for name in names_to_poll:
    if name in favorite_languages:
        print("Thank you for participating in our poll.")
    else:
        print("Hi, " + name.title() + " please take our poll.")
