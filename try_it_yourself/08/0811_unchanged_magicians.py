def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    great_magicians = []

    # BECOMING GREAT...
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append("The Great " + current_magician)

    return great_magicians

magicians = ['david blaine', 'houdini', 'mr mime']
great_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)