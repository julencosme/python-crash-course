# Movie Tickets: A movie theater charges different ticket prices depending
# on a person's age.
#
# If a person is under the age of 3, the ticket is free.
# If they are between 3 and 12, the ticket is $10.
# And if they are over age 12, the ticket is $15.
#
# Write a loop in which you ask users their age, and then tell them the cost of
# their movie ticket.

prompt = "What is your age?\n"
prompt += "Once you have entered your age, we will state your admission fee: "


while True:
    age = int(input(prompt))

    if age <= 3:
        print("Free admission")
    elif age > 3 and age <= 12:
        print("Ten dollars, please.")
    else:
        print("Fifteen dollars, please.")
