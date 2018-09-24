guest_list = ['jim', 'santa', 'poe']

print('Hey ' + guest_list[0].title() + ', ' + guest_list[1].title() + ' and ' + guest_list[2].title() + '!')
print('Would you like to join me for dinner?')
print('Let me know.')

print('\nLooks like ' + guest_list[2].title() + " can't make it.\n")

guest_list[2] = 'the rock'

print(guest_list[0].title() + '! Hope to see you there!')
print('Still coming over, ' + guest_list[1].title() + '.')
print('Come to dinner, ' + guest_list[2].title() + '.')