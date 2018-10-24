message = "So you want "
groceries = ['']
item_number = 0
end_word = ''

end_word = input("What word to end program? ")

print("\nEnter items in your grocery list.")
print("Enter '" + end_word + "' when finished.\n")

while groceries[-1].lower() != end_word:
    item_number += 1

    groceries.append(input("Item " + str(item_number) + ": "))

groceries = groceries[1:-1]

for item in groceries:
    if item == groceries[-1]:
        message += "and " + item + "?"
    else:
        message += item + ", "

print('\n' + message)
print("Got it!")