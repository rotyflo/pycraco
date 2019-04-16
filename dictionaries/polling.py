favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print("{}'s favorite language is {}.".format(name.title(), language.title()))

print("")

people_to_poll = ['jen', 'steve', 'phil', 'nick', 'sarah']

for name in people_to_poll:
    if name in favorite_languages.keys():
        print("Thanks for taking the poll, {}!".format(name.title()))
    else:
        print("Don't forget to take our poll, {}.".format(name.title()))