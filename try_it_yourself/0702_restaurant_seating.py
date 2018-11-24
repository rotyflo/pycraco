amount_of_people = input("How many people will be eating tonight? ")
amount_of_people = int(amount_of_people)

if amount_of_people > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Okay. You're table is ready!")