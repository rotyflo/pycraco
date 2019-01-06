guest_list = ['jim', 'santa', 'poe']

print('Hey ' + guest_list[0].title() + ', ' + guest_list[1].title() + ' and ' + guest_list[2].title() + '!')
print('Would you like to join me for dinner?')
print('Let me know.')

print('\nLooks like ' + guest_list[2].title() + " can't make it.\n")

guest_list[2] = 'the rock'

print(guest_list[0].title() + '! Hope to see you there!')
print('Still coming over, ' + guest_list[1].title() + '.')
print('Come to dinner, ' + guest_list[2].title() + '.')

print('\n... I found a bigger table.')

guest_list.insert(0, 'thing 1')
guest_list.insert(2, 'thing 2')
guest_list.append('the cat')

print('\n' + guest_list[0].title() + ', come and eat.')
print(guest_list[1].title() + ', come and eat.')
print(guest_list[2].title() + ', come and eat.')
print(guest_list[3].title() + ', come and eat.')
print(guest_list[4].title() + ', come and eat.')
print(guest_list[5].title() + ', come and eat.')

print('\nSorry guys, I can only invite 2 people for dinner.')

print('Sorry, ' + guest_list.pop().title() + ", you can't come.")
print('Sorry, ' + guest_list.pop().title() + ", you can't come.")
print('Sorry, ' + guest_list.pop().title() + ", you can't come.")
print('Sorry, ' + guest_list.pop(1).title() + ", you can't come.")

print('\n' + guest_list[0].title() + ' and ' + guest_list[1].title() + ', it is on. See you guys at 6.')

del guest_list[0]
del guest_list[0]

print(guest_list)