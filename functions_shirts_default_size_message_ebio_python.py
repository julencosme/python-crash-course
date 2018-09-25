# Large Shirts: Modify the 'make_shirt()' function so that shirts are large
# by default with a message that reads "I love Python".
#
# Make a a large shirt and a medium shirt with the default message, and a shirt
# of any size with a different message.


def make_shirt(size='large', message='I love Python'):
    """Display information regarding the size and message of a shirt, with a default size of large, and message of I love Python."""
    print("The shirt size is " + size +
          " and the message will read: " + message + ".")


make_shirt(message='I love Python')
make_shirt(message='I love Python', size='medium')
make_shirt(message='Evolutionary Biology & Ecology Club')
