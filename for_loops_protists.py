# Think of at least three different animals that have a common
# characteristic . Store the names of these animals in a list, 
# and then use a for loop to print out the name of each animal . 
# 
# Modify your program to print a statement about each animal, 
# such as A dog would make a great pet. 
# 
# Add a line at the end of your program stating what these animals
# have in common . 
# You could print a sentence such as Any of these animals would make 
# a great pet!

protists_chlorophyta = ['volvox', 'actinastrum', 'hydrodictyon']
for protist in protists_chlorophyta:
        print(protist)
for protist in protists_chlorophyta:
        print(protist.title() + ", is a protist in the green algae genus.")
print("All of these protists are in the division Chlorophyta, and they are photosynthetic organisms.")
