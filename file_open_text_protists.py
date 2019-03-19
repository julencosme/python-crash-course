# Opening text file: 'protists.txt' using a program that prints the text three different ways.
# The content focuses on protists.

with open('protists.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


filename = 'protists.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
