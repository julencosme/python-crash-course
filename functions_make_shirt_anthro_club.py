# T-Shirt: Write a function called 'make_shirt()' that accepts a size and
# the text of a message that should be printed on the shirt.
#
# The function should print a sentence summarizing the size of the shirt and the
# message printed on it.
#
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

# 'make_shirt()' function calling positional arguments.


def make_shirt(size, message):
    """Display information regarding the size and message of a shirt."""
    print("The shirt size is " + size +
          " and the message will read: " + message + ".")


make_shirt('large', 'Archaeology Club')

# 'make_shirt()' function calling keyword arguments.


def make_shirt(size, message):
    """Display information regarding the size and message of a shirt."""
    print("The shirt size is " + size +
          " and the message will read: " + message + ".")


make_shirt(size='large', message='Archaeology Club')
