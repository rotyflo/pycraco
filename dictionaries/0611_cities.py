cities = {
    'new york': {
        'country': 'the united states',
        'population': '8,622,698',
        'fact': 'the New York City Subway is the largest single-operator rapid transit system worldwide'
    },
    'tokyo': {
        'country': 'japan',
        'population': '13,839,910',
        'fact': 'it ranks first in the Global Economic Power Index'
    },
    'london': {
        'country': 'england',
        'population': '8,825,000',
        'fact': 'it is the most-visited city as measured by international arrivals and has the busiest city airport system as measured by passenger traffic'
    }
}

for city in cities:
    country = cities[city]['country']
    population = cities[city]['population']
    fact = cities[city]['fact']
    
    print(
        "\n{} is located in {} with a population of {} and {}."
        .format(
            city.title(),
            country.title(),
            str(population),
            fact
        )
    )