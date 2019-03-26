# Creating a guest book.

filename = 'guest_book.txt'

while True:
    name = input(
        '\nPlease enter your first and last name (type "quit" to quit): ')

    if name != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write('\n' + name)
            print('\nHello, ' + name + ': thank you for signing our guest book.')
    else:
        break
