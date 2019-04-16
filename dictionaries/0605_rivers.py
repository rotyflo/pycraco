rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'ob': 'russia'
}

print("\nSENTENCES")
for river, country in rivers.items():
    print("The {} river runs through {}.".format(river.title(), country.title()))

print("\nRIVERS")
for river in rivers.keys():
    print(river.title())

print("\nCOUNTRIES")
for country in rivers.values():
    print(country.title())

print("")