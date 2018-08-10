# Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
#
# Print the message, "The first three items in the list are:" . 
# Then use a slice to print the first three items from that program’s list .
#
# Print the message, "Three items from the middle of the list are:". 
# Use a slice to print three items from the middle of the list .
#
# Print the message, "The last three items in the list are:". 
# Use a slice to print the last three items in the list.
#
# Volvox = genus of chlorophytes. A type of green algae. Volvox forms spherical
# colonies (up to 50,000 cells). Live in freshwater habitats.
# First reported by Antonie van Leeuwenhoek in 1700. 
# Volvox developed its colonial lifestyle around 200 million years ago.

# Print the message, "The first three items in the list are:" . 
# Then use a slice to print the first three items from that program’s list .

protists_chlorophyta = ["volvox", "actinastrum", "hydrodictyon", "spirogyra"]
print("The first three items in the list are:")
for protist in protists_chlorophyta[:3]:
    print(protist.title())

# Print the message, "Three items from the middle of the list are:". 
# Use a slice to print three items from the middle of the list .

protists_chlorophyta = ["volvox", "actinastrum", "hydrodictyon", "spirogyra"]
print("The items in the middle of the list are:")
for protist in protists_chlorophyta[1:3]:
   print(protist.title())

# Print the message, "The last three items in the list are:".
# Use a slice to print the last three items in the list.

protists_chlorophyta= ["volvox", "actinastrum", "hydrodictyon", "spirogyra"]
print("The last three items in the list are:")
for protist in protists_chlorophyta[-3:]:
    print(protist.title())

