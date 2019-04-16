def describe_city(city, country='the united states'):
    print("{} is in {}.".format(city.title(), country.title()))

describe_city('corpus christi')
describe_city('tokyo', 'japan')
describe_city('san fransisco')