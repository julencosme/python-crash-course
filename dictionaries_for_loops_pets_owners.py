# Make several dictionaries, where the name of each dictionary is 
# the name of a pet. 
# 
# In each dictionary, include the kind of animal and the owner's name. 
# Store these dictionaries in a list called pets.
# 
# Next loop through your list and as you do print everything you know about
# each pet.

pets = {
    'chibbs': {
        'species_family': 'canidae',
        'owner_name': 'carolyn',
    },
    'scooter': {
        'species_family': 'canidae',
        'owner_name': 'bianca',
    },
    'inky': {
        'species_family': 'felidae',
        'owner_name': 'jaunita',
    },
    'sushi': {
        'species_family': 'felidae',
        'owner_name': 'gustav',
    },
    'chunky_monkey': {
        'species_family': 'cricetidae',
        'owner_name': 'luther',
    }
}

for pet, pet_info in pets.items():
    pet_type = pet_info['species_family']
    owner_first_name = pet_info['owner_name']
    print("\nPet: " + pet.title())
    print("\nPet type: " + pet_type.title())
    print("\nOwner's first name: " + owner_first_name.title())