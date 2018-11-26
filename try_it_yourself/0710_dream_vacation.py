vacation_poll = {}

while True:
    name = input("\nWhat is your name? ")
    location = input("Where would you like to go on vacation? ")

    vacation_poll[name] = location

    poll_again = input("Would someone else like to take the poll? (y/n) ")

    if poll_again.lower() == 'n':
        break

print("\n\t======== POLL RESULTS ========")
for name, location in vacation_poll.items():
    print("\t{} would like to go to {}.".format(name.title(), location.title()))
print("\t==============================")