# Ordinal Numbers: Ordinal numbers indicate their position in a list.
# 
# Store the numbers 1 through 9 in a list.
# 
# Loop through the list. Use an if-elif-else chain inside the loop to print the
# proper ordinal ending for each number. 
# 
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result
# should be on a separate line .

number_list= ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in number_list:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + "nd")
    elif number == '3':
        print(number + "rd")
    elif number == '4':
        print(number + "th")
    elif number == '5':
        print(number + "th")
    elif number == '6':
        print(number + "th")
    elif number == '7':
        print(number + "th")
    elif number == '8':
        print(number + "th")
else:
    print(number + "th")
