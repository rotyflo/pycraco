current_users = ['tim', 'rob', 'joe', 'Sue', 'jon']
new_users = ['timmy', 'robby', 'joey', 'sue', 'Jon']

lower_current_users = []
for user in current_users:
    lower_current_users.append(user.lower())

for user in new_users:
    if user.lower() in lower_current_users:
        print("Sorry, '" + user + "' is already taken.")
    else:
        print("User '" + user + "' created.")