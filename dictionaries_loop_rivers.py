major_rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yangtze': 'china',
}
for river in major_rivers:
    print("The " + river.title() + " runs through " +
          major_rivers[river].title() + ".")
