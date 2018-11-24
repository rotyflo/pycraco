prompt = "\nWhat pizza topping would you like?"
prompt += "\n(Enter 'quit' to exit the program) "
topping = input(prompt)

while True:
    if topping == 'quit':
        break
    else:
        print("\nOkay, I'll add " + topping + ".")
        topping = input("What else would you like? ")