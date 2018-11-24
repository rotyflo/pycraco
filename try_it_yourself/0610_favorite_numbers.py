fav_nums = {
    'steve': [3],
    'joe': [1, 7],
    'kyle': [2, 3],
    'jess': [9, 10, 33],
    'roy': [8]
}

for name, numbers in fav_nums.items():
    if len(numbers) == 1:
        print("\n{}'s favorite number is {}.".format(name.title(),
                                                   str(numbers[0])))
    else:
        print("\n{}'s favorite numbers are:".format(name.title()))
        for number in numbers:
            print("\t" + str(number))