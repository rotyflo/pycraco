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

print('\nI found a bigger dinner table!\n')

guests.insert(0, 'mo')
guests.insert(2, 'tommy')
guests.append('chris')

print(greeting + guests[0].title() + '? ' + invite)
print(greeting + guests[1].title() + '? ' + invite)
print(greeting + guests[2].title() + '? ' + invite)
print(greeting + guests[3].title() + '? ' + invite)
print(greeting + guests[4].title() + '? ' + invite)
print(greeting + guests[5].title() + '? ' + invite)

uninvite = "I'm sorry, but I can't invite you to dinner, "

print('\n' + uninvite + guests.pop().title())
print(uninvite + guests.pop().title())
print(uninvite + guests.pop().title())
print(uninvite + guests.pop().title())

still_invite = "My invitation still stands, "

print('\n' + still_invite + guests[0].title())
print(still_invite + guests[1].title())

del guests[0]
del guests[0]

print(guests)
