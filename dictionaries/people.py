people = [
    {
        'first_name': 'robert',
        'last_name': 'flores',
        'age': 26,
        'city': 'san antonio'
    },
    {
        'first_name': 'christian',
        'last_name': 'miller',
        'age': 32,
        'city': 'odessa'
    },
    {
        'first_name': 'jason',
        'last_name': 'smith',
        'age': 22,
        'city': 'corpus christi'
    }
]

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print("\n{} is a {} year old who lives in {}.".format(name, age, city))