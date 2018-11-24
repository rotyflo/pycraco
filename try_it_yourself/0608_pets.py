socks = {
    'name': 'socks',
    'type': 'cat',
    'owner': 'rt'
}
castle = {
    'name': 'castle',
    'type': 'dog',
    'owner': 'danny'
}
fluffy = {
    'name': 'fluffy',
    'type': 'mouse',
    'owner': 'chad'
}

pets = [socks, castle, fluffy]

for pet in pets:
    print("{} is {}'s {}.".format(pet['name'].title(),
                                  pet['owner'].title(),
                                  pet['type']))