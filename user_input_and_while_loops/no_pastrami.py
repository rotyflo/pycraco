sandwich_orders = [
    'tuna',
    'pastrami',
    'pastrami',
    'grilled cheese',
    'peanut butter',
    'pastrami'
]
finished_sandwiches = []

print("\nThe deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("\nI made your {} sandwich.".format(sandwich))

    finished_sandwiches.append(sandwich)

print("\nHere are all the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)