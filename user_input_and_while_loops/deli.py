sandwich_orders = ['tuna', 'grilled cheese', 'peanut butter']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("\nI made your {} sandwich.".format(sandwich))

    finished_sandwiches.append(sandwich)

print("\nHere are all the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)