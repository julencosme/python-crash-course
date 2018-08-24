# Rental Car: Write a program that asks the user what kind of rental car
# they would like.
#
# Print a message about that car, such as "Let me see if I can find you a
# Subaru".

prompt = "What kind of rental vehicle would you like? "
prompt+="Do you prefer a van, suv or sedan? "

rental = input(prompt)
print("Let us see if we can secure that " + rental + " for you.")

