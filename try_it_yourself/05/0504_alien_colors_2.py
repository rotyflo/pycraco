alien_color = input("Will you shoot down the red, yellow or green spaceship? ").lower()

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow' or alien_color == 'red':
    print("You earned 10 points!")
else:
    print("You missed!")