def make_car(manufacturer, model_name, **specs):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model_name
    for key, value in specs.items():
        car[key] = value
    return car

car = make_car('pontiac', 'vibe',
               color='grey',
               transmission='automatic')

print(car)