# Replacing the word 'protists' with 'Amoeba proteus' in file 'protists.txt'.

filename = 'protists.txt'
with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('protists', 'Amoeba proteus')
    print(contents)
