favorite_places = {
    'nick': ['texas'],
    'kim': ['florida', 'kansas', 'georgia'],
    'chad': ['california', 'washington']
}

for person, states in favorite_places.items():
    if len(states) == 1:
        print("\n{}'s favorite place is {}.".format(person.title(),
                                                    states[0].title()))
    else:
        print("\n{}'s favorite places are:".format(person.title()))
        for state in states:
            print("\t" + state.title())