guests = ['walter', 'tanaka', 'mo']
greeting = 'How are you, '
invite = 'Would you like to come to dinner?'

print(greeting + guests[0].title() + '? ' + invite)
print(greeting + guests[1].title() + '? ' + invite)
print(greeting + guests[2].title() + '? ' + invite)

print('\nIt looks like ' + guests[2].title() + ' can\'t make it.\n')

guests[2] = 'steven'

print(greeting + guests[0].title() + '? ' + invite)
print(greeting + guests[1].title() + '? ' + invite)
print(greeting + guests[2].title() + '? ' + invite)
