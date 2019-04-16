while True:
    print("('quit' to exit)")
    age = input("How old are you? ")
    
    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            print("\nYour ticket is free!")
        elif age <= 12:
            print("\nThat'll be $10!")
        else:
            print("\nThat'll be $15!")