protists_chlorophyta = ["volvox", "actinastrum", "hydrodictyon", "spirogyra"]
print("The first three items in the list are:")
for protist in protists_chlorophyta[:3]:
    print(protist.title())

protists_chlorophyta = ["volvox", "actinastrum", "hydrodictyon", "spirogyra"]
print("The items in the middle of the list are:")
for protist in protists_chlorophyta[1:3]:
    print(protist.title())


protists_chlorophyta = ["volvox", "actinastrum", "hydrodictyon", "spirogyra"]
print("The last three items in the list are:")
for protist in protists_chlorophyta[-3:]:
    print(protist.title())
