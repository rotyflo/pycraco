users = ['admin', 'joe', 'sara']

username = input("username: ")

if username.lower() in users:
    password = input("password: ")

    if password == 'password':
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")
