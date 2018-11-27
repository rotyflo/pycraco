def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    great_magicians = []

    # BECOMING GREAT...
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append("The Great " + current_magician)

    # MAGICIANS HAVE BECOME GREAT!
    while great_magicians:
        current_magician = great_magicians.pop()
        magicians.append(current_magician)

magicians = ['david blaine', 'houdini', 'mr mime']

make_great(magicians)
show_magicians(magicians)