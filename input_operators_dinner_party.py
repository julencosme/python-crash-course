# Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. 
# 
# If the answer is more than eight, print a message saying they'll have to wait
# for a table. Otherwise, report that their table is ready.

dinner_party = input("How many people are in your dinner party group? ")
dinner_party = int(dinner_party)

if dinner_party > 8:
    print("You will have to wait for a table, thank you for your patience.")
else:
    print("Your table is ready!")

    

