def city_country(city, country):
    formatted_location = "{}, {}".format(city.title(), country.title())
    return formatted_location

my_town = city_country('san antonio', 'the united states')
your_town = city_country('santiago', 'chile')
their_town = city_country('tokyo', 'japan')

print(my_town)
print(your_town)
print(their_town)