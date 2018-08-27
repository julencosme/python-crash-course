# Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
#
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

major_rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yangtze': 'china',
}
for river in major_rivers:
    print("The " + river.title() + " runs through " + major_rivers[river].title() + ".")
    
    