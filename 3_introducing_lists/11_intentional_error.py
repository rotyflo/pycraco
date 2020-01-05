guests = ['walter', 'tanaka', 'mo']
greeting = 'How are you, '
invite = 'Would you like to come to dinner?'

print(greeting + guests[0].title() + '? ' + invite)
print(greeting + guests[1].title() + '? ' + invite)
print(greeting + guests[2].title() + '? ' + invite)

# IndexError
print('\n' + guests[3].title())
