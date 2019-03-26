# Program to store lab notes concerning protists.

filename = 'protist_lab_notes.txt'

while True:
    observation = input(
        '\nPlease enter your lab notes (type "quit" to quit): ')

    if observation != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write('\n' + observation)
            print('\nObservation submitted.')
    else:
        break
